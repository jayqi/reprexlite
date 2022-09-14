from contextlib import redirect_stdout
from dataclasses import dataclass
from io import StringIO
from itertools import chain
from pathlib import Path
from pprint import pformat
import traceback
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

import libcst as cst

from reprexlite.config import ParsingMethod, ReprexConfig, format_args_google_style
from reprexlite.formatting import venues_dispatcher
from reprexlite.parsing import LineType, auto_parse, parse
from reprexlite.version import __version__

NO_RAW_VALUE = object()
"""Explicit placeholder object for results of statements, which have no return value (as opposed to
expressions)."""


@dataclass
class RawResult:
    """Class that holds the result of evaluated code. Use `str(...)` on an instance to produce a
    pretty-formatted comment block representation of the result.

    Attributes:
        config (ReprexConfig): Configuration for formatting and parsing
        raw (Any): Some Python object that is the raw return value of evaluated Python code.
        stdout (str): Standard output from evaluated Python code.
    """

    config: ReprexConfig
    raw: Any = NO_RAW_VALUE
    stdout: Optional[str] = None

    def __str__(self) -> str:
        lines = []
        if self.stdout:
            lines.extend(self.stdout.split("\n"))
        if self.raw is not NO_RAW_VALUE and (self.raw is not None or not self.stdout):
            # NO_RAW_VALUE -> don't print
            # None and stdout -> don't print
            # None and no stdout -> print
            # Anything else -> print
            lines.extend(pformat(self.raw, indent=2, width=77).split("\n"))
        return "\n".join(f"{self.config.comment} " + line for line in lines)

    def __bool__(self) -> bool:
        # If result is NO_RETURN and blank stdout, nothing to print
        return self.raw is not NO_RAW_VALUE or bool(self.stdout)

    def __repr__(self) -> str:
        return f"<RawResult '{to_snippet(str(self.raw), 10)}'>"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, RawResult):
            return self.raw == other.raw and self.stdout == other.stdout
        elif isinstance(other, ParsedResult):
            return str(self) == other.as_result_str()
        else:
            return False


@dataclass
class ParsedResult:
    """Class that holds parsed result from reading a reprex.

    Attributes:
        config (ReprexConfig): Configuration for formatting and parsing
        lines (List[str]): String content of result parsed from a reprex
    """

    config: ReprexConfig
    lines: List[str]

    def __str__(self) -> str:
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
        return bool(self.lines)

    def __repr__(self) -> str:
        joined = "\n".join(self.lines)
        return f"<ParsedResult '{to_snippet(joined, 10)}'>"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ParsedResult):
            return self.lines == other.lines
        elif isinstance(other, RawResult):
            return self.as_result_str() == str(other)
        else:
            return False


@dataclass
class NullResult:
    config: ReprexConfig

    def __str__(self) -> str:
        raise NotImplementedError

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "<NullResult>"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, NullResult):
            return True
        else:
            return False


@dataclass
class Statement:
    """Class that holds a LibCST parsed statement. The evaluate method will evaluate the statement
    and return a [`Result`][reprexlite.code.Result] object. To recover the original source code
    for an instancement, call `str(...)` on it. You can optionally autoformat the returned source
    code, controlled by the `style` attribute.

    Attributes:
        config (ReprexConfig): Configuration for formatting and parsing
        stmt (Union[libcst.SimpleStatementLine, libcst.BaseCompoundStatement]): LibCST parsed
            statement.
    """

    config: ReprexConfig
    stmt: Union[cst.SimpleStatementLine, cst.BaseCompoundStatement, cst.EmptyLine]

    def evaluate(self, scope: dict) -> Union[RawResult, NullResult]:
        if isinstance(self.stmt, cst.EmptyLine):
            return NullResult(config=self.config)

        if "__name__" not in scope:
            scope["__name__"] = "__reprex__"
        stdout_io = StringIO()
        try:
            with redirect_stdout(stdout_io):
                try:
                    result = eval(str(self).strip(), scope)
                except SyntaxError:
                    exec(str(self).strip(), scope)
                    result = NO_RAW_VALUE
            stdout = stdout_io.getvalue().strip()
        except Exception as exc:
            result = NO_RAW_VALUE
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

        if (result is NO_RAW_VALUE or result is None) and not stdout:
            return NullResult(config=self.config)
        else:
            return RawResult(config=self.config, raw=result, stdout=stdout)

    @property
    def raw_code(self):
        return cst.Module(body=[self.stmt]).code.rstrip()

    @property
    def code(self):
        code = self.raw_code
        if self.config.style:
            try:
                from black import Mode, format_str
            except ImportError:
                raise ImportError("Must install black to restyle code.")

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

    def __bool__(self):
        return True

    def __repr__(self) -> str:
        return f"<Statement '{to_snippet(self.code, 10)}'>"


@dataclass
class Reprex:
    """Container class for a reprex, which holds Python code and results from evaluation.

    Attributes:
        config (ReprexConfig): Configuration for formatting and parsing
        statements (List[Statement]): List of parsed Python code statements
        results (List[Union[RawResult, NullResult]]): List of results evaluated from statements
        old_results (List[Union[ParsedResult, NullResult]]): List of any old results parsed from
            input code
        scope (Dict[str, Any]): Dictionary holding the scope that the reprex was evaluated in.
    """

    config: ReprexConfig
    statements: List[Statement]
    results: List[Union[RawResult, NullResult]]
    old_results: List[Union[ParsedResult, NullResult]]
    scope: Dict[str, Any]

    def __post_init__(self):
        if len(self.statements) != len(self.results) != len(self.results):
            raise Exception

    @classmethod
    def from_input(
        cls,
        input: str,
        config: Optional[ReprexConfig] = None,
        scope: Optional[Dict[str, Any]] = None,
    ):
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
            raise Exception
        return cls.from_input_lines(lines, config=config, scope=scope)

    @classmethod
    def from_input_lines(
        cls,
        lines: Sequence[Tuple[str, LineType]],
        config: Optional[ReprexConfig] = None,
        scope: Optional[Dict[str, Any]] = None,
    ):
        if config is None:
            config = ReprexConfig()
        statements: List[Statement] = []
        old_results: List[Union[ParsedResult, NullResult]] = []
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
                    # Pad results with NullResults
                    old_results += [NullResult(config=config)] * (len(new_statements) - 1)
                    # Reset current code block
                    current_code_block = []
                # Append line to current results
                current_result_block.append(line_content)
        # Flush code
        if current_code_block:
            if all(not line for line in current_code_block):
                # Case where all lines are whitespace
                new_statements = [
                    Statement(config=config, stmt=cst.EmptyLine()) for _ in current_code_block
                ]
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
            # Pad results with NullResults
            statements += new_statements
            old_results += [NullResult(config=config)] * (len(new_statements) - 1)
        # Flush results
        if current_result_block:
            # Create result
            old_results += [ParsedResult(config=config, lines=current_result_block)]
            # Result current result block
            current_result_block = []
        # Pad results to equal length
        old_results += [NullResult(config=config)] * (len(statements) - len(old_results))

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

    def __str__(self) -> str:
        if self.config.keep_old_results:
            lines = chain.from_iterable(zip(self.statements, self.old_results, self.results))
        else:
            lines = chain.from_iterable(zip(self.statements, self.results))
        return "\n".join(str(line) for line in lines if line)

    def format(self, terminal: bool = False):
        out = str(self)
        if terminal:
            try:
                from pygments import highlight
                from pygments.formatters import Terminal256Formatter
                from pygments.lexers import PythonLexer

                out = highlight(out, PythonLexer(), Terminal256Formatter(style="friendly"))
            except ImportError:
                pass
        formatter = venues_dispatcher[self.config.venue]
        return formatter.format(
            out.strip(), advertise=self.config.advertise, session_info=self.config.session_info
        )

    def _repr_html_(self):
        out = []
        try:
            from pygments import highlight
            from pygments.formatters import HtmlFormatter
            from pygments.lexers import PythonLexer

            formatter = HtmlFormatter(style="friendly", wrapcode=True)
            out.append(f"<style>{formatter.get_style_defs('.highlight')}</style>")
            out.append(highlight(self.format(), PythonLexer(), formatter))
        except ImportError:
            out.append(f"<pre><code>{self.format()}</code></pre>")
        return "\n".join(out)

    def results_match(self):
        return all(
            result == old_result for result, old_result in zip(self.results, self.old_results)
        )


def to_snippet(s: str, n: int):
    if len(s) <= n:
        return rf"{s}"
    else:
        return rf"{s[:n]}..."


def reprex(
    input: str,
    outfile: Optional[Path] = None,
    print_=True,
    terminal=False,
    **kwargs,
) -> Reprex:
    """Render reproducible examples of Python code for sharing. This function will evaluate your
    code and, by default, print out your code with the evaluated results embedded as comments,
    along with additional markup appropriate to the sharing venue set by the `venue` keyword
    argument. The function returns an instance of [`Reprex`][reprexlite.reprexes.Reprex] which
    holds the relevant data.

    For example, for the `gh` venue for GitHub Flavored Markdown, you'll get a reprex whose
    formatted output looks like:

    ````
    ```python
    x = 2
    x + 2
    #> 4
    ```

    <sup>Created at 2021-02-15 16:58:47 PST by [reprexlite](https://github.com/jayqi/reprexlite) v{{version}}</sup>
    ````

    The supported `venue` formats are:

    - `gh` : GitHub Flavored Markdown
    - `so` : StackOverflow, alias for gh
    - `ds` : Discourse, alias for gh
    - `html` : HTML
    - `py` : Python script
    - `rtf` : Rich Text Format
    - `slack` : Slack

    Args:
    {{args}}

    Returns:
        Instance of `Reprex`
    """

    config = ReprexConfig(**kwargs)
    if config.venue in ["html", "rtf"]:
        # Don't screw up output file or lexing for HTML and RTF with terminal syntax highlighting
        terminal = False
    reprex = Reprex.from_input(input, config=config)
    formatted_reprex = reprex.format(terminal=terminal)
    if outfile is not None:
        with outfile.open("w") as fp:
            fp.write(reprex.format(terminal=False))
    if print_:
        print(formatted_reprex)
    return formatted_reprex


if reprex.__doc__:
    reprex.__doc__ = reprex.__doc__.replace("{{version}}", __version__).replace(
        "{{args}}", format_args_google_style()
    )
