from contextlib import redirect_stdout
import dataclasses
from io import StringIO
from itertools import chain
import os
from pathlib import Path
from pprint import pformat
import traceback
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

try:
    from typing import Self  # type: ignore  # Python 3.11+
except ImportError:
    from typing_extensions import Self

import libcst as cst

from reprexlite.config import ParsingMethod, ReprexConfig
from reprexlite.exceptions import BlackNotFoundError, UnexpectedError
from reprexlite.formatting import formatter_registry
from reprexlite.parsing import LineType, auto_parse, parse


@dataclasses.dataclass
class RawResult:
    """Class that holds the result of evaluated code. Use `str(...)` on an instance to produce a
    pretty-formatted comment block representation of the result.

    Attributes:
        config (ReprexConfig): Configuration for formatting and parsing
        raw (Any): Some Python object that is the raw return value of evaluated Python code.
        stdout (str): Standard output from evaluated Python code.
    """

    config: ReprexConfig
    raw: Any
    stdout: Optional[str]

    def __str__(self) -> str:
        if not self:
            raise UnexpectedError("Should not print a RawResult if it tests False.")
        lines = []
        if self.stdout:
            lines.extend(self.stdout.split("\n"))
        if self.raw is not None:
            lines.extend(pformat(self.raw, indent=2, width=77).split("\n"))
        return "\n".join(f"{self.config.comment} " + line for line in lines)

    def __bool__(self) -> bool:
        """Tests whether instance contains anything to print."""
        return not (self.raw is None and self.stdout is None)

    def __repr__(self) -> str:
        return (
            f"<RawResult '{to_snippet(str(self.raw), 10)}' '{to_snippet(str(self.stdout), 10)}'>"
        )

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, RawResult):
            return self.raw == other.raw and self.stdout == other.stdout
        else:
            return NotImplemented


@dataclasses.dataclass
class ParsedResult:
    """Class that holds parsed result from reading a reprex.

    Attributes:
        config (ReprexConfig): Configuration for formatting and parsing
        lines (List[str]): String content of result parsed from a reprex
    """

    config: ReprexConfig
    lines: List[str]

    def __str__(self) -> str:
        if not self:
            raise UnexpectedError("Should not print a ParsedResult if it tests False.")
        return "\n".join(self.prefix * 2 + line for line in self.lines)

    def as_result_str(self) -> str:
        return "\n".join(self.prefix + line for line in self.lines)

    @property
    def prefix(self) -> str:
        if self.config.comment:
            return self.config.comment + " "
        else:
            return ""

    def __bool__(self) -> bool:
        """Tests whether instance contains anything to print."""
        return bool(self.lines)

    def __repr__(self) -> str:
        joined = "\\n".join(self.lines)
        return f"<ParsedResult '{to_snippet(joined, 10)}'>"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ParsedResult):
            return self.lines == other.lines
        elif isinstance(other, RawResult):
            if not bool(self) and not bool(other):
                return True
            return bool(self) and bool(other) and self.as_result_str() == str(other)
        else:
            return NotImplemented


@dataclasses.dataclass
class Statement:
    """Dataclass that holds a LibCST parsed statement. of code.

    Attributes:
        config (ReprexConfig): Configuration for formatting and parsing
        stmt (Union[libcst.SimpleStatementLine, libcst.BaseCompoundStatement]): LibCST parsed
            statement.
    """

    config: ReprexConfig
    stmt: Union[cst.SimpleStatementLine, cst.BaseCompoundStatement, cst.EmptyLine]

    def evaluate(self, scope: dict) -> RawResult:
        """Evaluate code statement and produce a RawResult dataclass instance.

        Args:
            scope (dict): scope to use for evaluation

        Returns:
            RawResult: Dataclass instance holding evaluation results.
        """
        if isinstance(self.stmt, cst.EmptyLine):
            return RawResult(config=self.config, raw=None, stdout=None)

        if "__name__" not in scope:
            scope["__name__"] = "__reprex__"
        stdout_io = StringIO()
        try:
            with redirect_stdout(stdout_io):
                try:
                    # Treat as a single expression
                    result = eval(self.code.strip(), scope)
                except SyntaxError:
                    # Treat as a statement
                    exec(self.code.strip(), scope)
                    result = None
            stdout = stdout_io.getvalue().strip()
        except Exception as exc:
            result = None
            # Skip first step of traceback, since that is this evaluate method
            if exc.__traceback__ is not None:
                tb = exc.__traceback__.tb_next
                stdout = (
                    "Traceback (most recent call last):\n"
                    + "".join(line for line in traceback.format_tb(tb))
                    + f"{type(exc).__name__}: {exc}"
                )
        finally:
            stdout_io.close()

        return RawResult(config=self.config, raw=result, stdout=stdout or None)

    @property
    def raw_code(self) -> str:
        """Raw code of contained statement as a string."""
        if isinstance(self.stmt, cst.EmptyLine):
            return cst.Module(body=[], header=[self.stmt]).code.rstrip()
        return cst.Module(body=[self.stmt]).code.rstrip()

    @property
    def code(self) -> str:
        """Code of contained statement. May be autoformatted depending on configuration."""
        code = self.raw_code
        if self.config.style:
            try:
                from black import Mode, format_str
            except ModuleNotFoundError as e:
                if e.name == "black":
                    raise BlackNotFoundError("Must install black to restyle code.", name="black")
                else:
                    raise

            code = format_str(code, mode=Mode())
        return code

    def __str__(self) -> str:
        out = self.code
        if self.config.prompt:
            # Add prompt and continuation prefixes to lines
            lines = out.split("\n")
            primary_found = False
            out = ""
            for line in lines:
                if line.strip() == "":
                    # Whitespace line
                    out += f"{self.config.prompt} " + line + "\n"
                elif line.startswith("#"):
                    # Comment line
                    out += f"{self.config.prompt} " + line + "\n"
                else:
                    # Code line
                    if not primary_found:
                        out += f"{self.config.prompt} " + line + "\n"
                        primary_found = True
                    else:
                        out += f"{self.config.continuation} " + line + "\n"
        return out.rstrip()

    def __bool__(self) -> bool:
        """Tests whether this instance contains anything to print. Always true for Statement."""
        return True

    def __repr__(self) -> str:
        return f"<Statement '{to_snippet(self.code, 10)}'>"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Statement):
            return self.raw_code == other.raw_code
        return NotImplemented


@dataclasses.dataclass
class Reprex:
    """Dataclass for a reprex, which holds Python code and results from evaluation.

    Attributes:
        config (ReprexConfig): Configuration for formatting and parsing
        statements (List[Statement]): List of parsed Python code statements
        results (List[RawResult]): List of results evaluated from statements
        old_results (List[ParsedResult]): List of any old results parsed from input code
        scope (Dict[str, Any]): Dictionary holding the scope that the reprex was evaluated in
    """

    config: ReprexConfig
    statements: List[Statement]
    results: List[RawResult]
    old_results: List[ParsedResult]
    scope: Dict[str, Any]

    def __post_init__(self) -> None:
        if not (len(self.statements) == len(self.results) == len(self.old_results)):
            raise UnexpectedError(
                "statements, results, and old_results should all be the same length. "
                f"Got: {(len(self.statements), len(self.results), len(self.old_results))}."
            )

    @classmethod
    def from_input(
        cls,
        input: str,
        config: Optional[ReprexConfig] = None,
        scope: Optional[Dict[str, Any]] = None,
    ) -> Self:
        """Create a Reprex instance from parsing and evaluating code from a string.

        Args:
            input (str): Input code
            config (Optional[ReprexConfig], optional): Configuration. Defaults to None, which will
                use default settings.
            scope (Optional[Dict[str, Any]], optional): Dictionary holding scope that the parsed
                code will be evaluated with. Defaults to None, which will create an empty
                dictionary.

        Returns:
            Reprex: New instance of Reprex.
        """
        if config is None:
            config = ReprexConfig()
        if config.parsing_method == ParsingMethod.AUTO:
            lines = list(auto_parse(input))
        elif config.parsing_method == ParsingMethod.DECLARED:
            lines = list(
                parse(
                    input,
                    prompt=config.resolved_input_prompt,
                    continuation=config.resolved_input_continuation,
                    comment=config.resolved_input_comment,
                )
            )
        else:
            raise UnexpectedError(  # pragma: nocover
                f"Parsing method {config.parsing_method} is not implemented."
            )
        return cls.from_input_lines(lines, config=config, scope=scope)

    @classmethod
    def from_input_lines(
        cls,
        lines: Sequence[Tuple[str, LineType]],
        config: Optional[ReprexConfig] = None,
        scope: Optional[Dict[str, Any]] = None,
    ) -> Self:
        """Creates a Reprex instance from the output of [parse][reprexlite.parsing.parse].

        Args:
            lines (Sequence[Tuple[str, LineType]]): Output from parse.
            config (Optional[ReprexConfig], optional): Configuration. Defaults to None, which will
                use default settings.
            scope (Optional[Dict[str, Any]], optional): Dictionary holding scope that the parsed
                code will be evaluated with. Defaults to None, which will create an empty
                dictionary.

        Returns:
            Reprex: New instance of Reprex.
        """
        if config is None:
            config = ReprexConfig()
        statements: List[Statement] = []
        old_results: List[ParsedResult] = []
        current_code_block: List[str] = []
        current_result_block: List[str] = []
        for line_content, line_type in lines:
            if line_type is LineType.CODE:
                # Flush results
                if current_result_block:
                    old_results += [ParsedResult(config=config, lines=current_result_block)]
                    current_result_block = []
                # Append line to current code
                current_code_block.append(line_content)
            elif line_type is LineType.RESULT:
                # Flush code
                if current_code_block:
                    # Parse code and create Statements
                    tree: cst.Module = cst.parse_module("\n".join(current_code_block))
                    new_statements = (
                        [Statement(config=config, stmt=stmt) for stmt in tree.header]
                        + [Statement(config=config, stmt=stmt) for stmt in tree.body]
                        + [Statement(config=config, stmt=stmt) for stmt in tree.footer]
                    )
                    statements += new_statements
                    # Pad results with empty results, 1 fewer because of current_result_block
                    old_results += [ParsedResult(config=config, lines=[])] * (
                        len(new_statements) - 1
                    )
                    # Reset current code block
                    current_code_block = []
                # Append line to current results
                current_result_block.append(line_content)
        # Flush code
        if current_code_block:
            if all(not line for line in current_code_block):
                # Case where all lines are whitespace: strip and don't add
                new_statements = []
            else:
                # Parse code and create Statements
                tree: cst.Module = cst.parse_module(  # type: ignore[no-redef]
                    "\n".join(current_code_block)
                )
                new_statements = (
                    [Statement(config=config, stmt=stmt) for stmt in tree.header]
                    + [Statement(config=config, stmt=stmt) for stmt in tree.body]
                    + [Statement(config=config, stmt=stmt) for stmt in tree.footer]
                )
            # Pad results with empty results, 1 fewer because of current_result_block
            statements += new_statements
            old_results += [ParsedResult(config=config, lines=[])] * (len(new_statements) - 1)
        # Flush results
        if current_result_block:
            old_results += [ParsedResult(config=config, lines=current_result_block)]
        # Pad results to equal length
        old_results += [ParsedResult(config=config, lines=[])] * (
            len(statements) - len(old_results)
        )

        # Evaluate for new results
        if scope is None:
            scope = {}
        results = [statement.evaluate(scope=scope) for statement in statements]
        return cls(
            config=config,
            statements=statements,
            results=results,
            old_results=old_results,
            scope=scope,
        )

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Reprex):
            return (
                self.config == other.config
                and all(left == right for left, right in zip(self.statements, other.statements))
                and all(left == right for left, right in zip(self.results, other.results))
                and all(left == right for left, right in zip(self.old_results, other.old_results))
            )
        else:
            return NotImplemented

    def __str__(self) -> str:
        if self.config.keep_old_results:
            lines = chain.from_iterable(zip(self.statements, self.old_results, self.results))
        else:
            lines = chain.from_iterable(zip(self.statements, self.results))
        out = "\n".join(str(line) for line in lines if line)
        if not out.endswith("\n"):
            out += "\n"
        return out

    @property
    def results_match(self) -> bool:
        """Whether results of evaluating code match old results parsed from input."""
        return all(
            result == old_result for result, old_result in zip(self.results, self.old_results)
        )

    def format(self) -> str:
        formatter = formatter_registry[self.config.venue]
        return formatter.format(
            str(self).strip(),
            advertise=self.config.advertise,
            session_info=self.config.session_info,
        )

    def print_formatted(self, **kwargs) -> None:
        formatter = formatter_registry[self.config.venue]
        formatter.print(
            str(self).strip(),
            advertise=self.config.advertise,
            session_info=self.config.session_info,
            **kwargs,
        )

    def __repr__(self) -> str:
        return f"<Reprex ({len(self.statements)}) '{to_snippet(str(self), 10)}'>"

    def _repr_html_(self) -> str:
        """HTML representation. Used for rendering in Jupyter."""
        out = []
        try:
            from pygments import highlight
            from pygments.formatters import HtmlFormatter
            from pygments.lexers import PythonLexer

            formatter = HtmlFormatter(style="friendly", wrapcode=True)
            out.append(f"<style>{formatter.get_style_defs('.highlight')}</style>")
            out.append(highlight(self.format(), PythonLexer(), formatter))
        except ModuleNotFoundError:
            out.append(f"<pre><code>{self.format()}</code></pre>")
        return "\n".join(out)


def to_snippet(s: str, n: int) -> str:
    if len(s) <= n:
        return rf"{s}"
    else:
        return rf"{s[:n]}..."


def reprex(
    input: str,
    outfile: Optional[Union[str, os.PathLike]] = None,
    print_: bool = True,
    config: Optional[ReprexConfig] = None,
    **kwargs,
) -> Reprex:
    """A convenient functional interface to render reproducible examples of Python code for
    sharing. This function will evaluate your code and, by default, print out your code with the
    evaluated results embedded as comments, formatted with additional markup appropriate to the
    sharing venue set by the `venue` keyword argument. The function returns an instance of
    [`Reprex`][reprexlite.reprexes.Reprex] which holds the relevant data.

    For example, for the `gh` venue for GitHub Flavored Markdown, you'll get a reprex whose
    formatted output looks like:

    ````
    ```python
    x = 2
    x + 2
    #> 4
    ```

    <sup>Created at 2021-02-15 16:58:47 PST by [reprexlite](https://github.com/jayqi/reprexlite)</sup>
    ````


    Args:
        input (str): Input code to create a reprex for.
        outfile (Optional[str | os.PathLike]): If provided, path to write formatted reprex
            output to. Defaults to None, which does not write to any file.
        print_ (bool): Whether to print formatted reprex output to console.
        config (Optional[ReprexConfig]): Instance of the configuration dataclass. Default of none
            will instantiate one with default values.
        **kwargs: Configuration options from [ReprexConfig][reprexlite.config.ReprexConfig]. Any
            provided values will override values from provided config or the defaults.

    Returns:
        (Reprex) Reprex instance
    """  # noqa: E501

    if config is None:
        config = ReprexConfig(**kwargs)
    else:
        config = dataclasses.replace(config, **kwargs)

    config = ReprexConfig(**kwargs)
    r = Reprex.from_input(input, config=config)
    if outfile is not None:
        with Path(outfile).open("w") as fp:
            fp.write(r.format())
    if print_:
        r.print_formatted()
    return r
