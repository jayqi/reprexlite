from contextlib import redirect_stdout
from dataclasses import dataclass
from io import StringIO
from itertools import chain
from pprint import pformat
import traceback
from typing import Any, List, Optional, Union

import libcst as cst

from reprexlite.exceptions import MissingDependencyError, PromptLengthMismatchError

NO_RETURN = object()
"""Explicit placeholder object for statements, which have no return value (as opposed to
expressions)."""

DEFAULT_COMMENT = "#>"
DEFAULT_PROMPT = ""
DEFAULT_CONTINUATION = ""


@dataclass
class Result:
    """Class that holds the result of evaluated code. Use `format` method to produce a
    pretty-formatted comment block representation of the result.

    Attributes:
        result (Any): Some Python object, intended to be the return value of evaluated Python code.
        stdout (Optional[str]): Any content captured from standard output.
    """

    result: Any
    stdout: Optional[str] = None

    def __str__(self) -> str:
        return self.format() or ""

    def format(self, comment: str = DEFAULT_COMMENT) -> Optional[str]:
        lines = []

        if self.stdout:
            lines.extend(self.stdout.split("\n"))

        if self.result is not NO_RETURN and (self.result is not None or not self.stdout):
            # NO_RETURN -> don't print result
            # None and stdout -> don't print result
            # None and no stdout -> print result
            # Anything else -> print result
            lines.extend(pformat(self.result, indent=2, width=77).split("\n"))

        if comment:
            prefix = comment + " "
        else:
            prefix = ""

        if lines:
            return "\n".join(prefix + line for line in lines)
        else:
            return None

    def __bool__(self) -> bool:
        # If result is NO_RETURN and blank stdout, nothing to print
        return self.result is not NO_RETURN or bool(self.stdout)


@dataclass
class Statement:
    """Class that holds a LibCST parsed statement. The evaluate method will evaluate the statement
    and return a [`Result`][reprexlite.code.Result] object. To recover the original source code
    for an instancement, call `str(...)` on it. You can optionally autoformat the returned source
    code, controlled by the `style` attribute.

    Attributes:
        stmt (Union[libcst.SimpleStatementLine, libcst.BaseCompoundStatement]): LibCST parsed
            statement.
    """

    stmt: Union[cst.EmptyLine, cst.BaseStatement]

    @property
    def code(self):
        return cst.Module(body=[self.stmt]).code

    def evaluate(self, scope: dict) -> Result:
        stdout_io = StringIO()
        try:
            with redirect_stdout(stdout_io):
                try:
                    result = eval(self.code.strip(), scope, scope)
                except SyntaxError:
                    exec(self.code.strip(), scope, scope)
                    result = NO_RETURN
            stdout = stdout_io.getvalue().strip()
        except Exception as exc:
            result = NO_RETURN
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
        return Result(result, stdout=stdout)

    def __str__(self) -> str:
        return self.format()

    def format(
        self, style: bool = False, prompt: str = DEFAULT_PROMPT, continuation=DEFAULT_CONTINUATION
    ):
        validate_prompts(prompt, continuation)

        out = self.code

        if style:
            try:
                from black import Mode, format_str
            except ImportError:
                raise MissingDependencyError("Must install black to restyle code.")

            out = format_str(out, mode=Mode())

        if out.endswith("\n"):
            # Strip trailing newline without stripping deliberate ones.
            out = out[:-1]

        if prompt:
            # Add prompt and continuation prefixes to lines
            lines = out.split("\n")
            primary_found = False
            out = ""
            for line in lines:
                if line.strip() == "":
                    # Whitespace line
                    out += f"{prompt} " + line
                else:
                    # Code line
                    if not primary_found:
                        out += f"{prompt} " + line
                        primary_found = True
                    else:
                        out += f"\n{continuation} " + line
        return out


def validate_prompts(prompt: str, continuation: str):
    if len(prompt) != len(continuation):
        raise PromptLengthMismatchError(
            f"Primary prompt ('{prompt}') and continuation prompt ('{continuation}') must be "
            "equal lengths."
        )


@dataclass
class CodeBlock:
    """Class that takes a block of Python code input and evaluates it. Call `str(...)` on an
    instance to get back a string containing the original source with evaluated outputs embedded
    as comments below each statement.

    Attributes:
        statements (List[Statement]): List of individual statements parsed from input code.
        results (List[Result]): List of evaluated results corresponding to each item of statements.
        _code (Optional[str]): Input block of Python code. Only set if instance is created by
            parse_and_evaluate class method.
        _tree (Optional[libcst.Module]): Parsed LibCST concrete syntax tree of input code. Only set
            if instance is created by parse_and_evaluate class method.
        _namespace (Optional[dict]): Namespace used as scope for evaluating statements. Only set if
            instance is created by parse_and_evaluate class method.
    """

    statements: List[Statement]
    results: List[Result]
    _code: Optional[str] = None
    _tree: Optional[cst.Module] = None
    _namespace: Optional[dict] = None

    @classmethod
    def parse_and_evaluate(cls, code: str) -> "CodeBlock":
        # Parse code
        tree: cst.Module = cst.parse_module(code)
        statements: List[Statement] = (
            [Statement(header) for header in tree.header]
            + [Statement(stmt) for stmt in tree.body]
            + [Statement(footer) for footer in tree.footer]
        )
        # Evaluate code
        namespace: dict = {}
        results: List[Result] = [stmt.evaluate(namespace) for stmt in statements]
        return cls(
            statements=statements, results=results, _code=code, _tree=tree, _namespace=namespace
        )

    def format(
        self,
        style: bool = False,
        prompt: str = DEFAULT_PROMPT,
        continuation: str = DEFAULT_CONTINUATION,
        comment: str = DEFAULT_COMMENT,
        terminal=False,
    ):
        statements = (
            statement.format(style=style, prompt=prompt, continuation=continuation)
            for statement in self.statements
        )
        results = (result.format(comment=comment) for result in self.results)
        out = "\n".join(line for line in chain.from_iterable(zip(statements, results)) if line)
        if terminal:
            try:
                from pygments import highlight
                from pygments.formatters import Terminal256Formatter
                from pygments.lexers import PythonLexer

                out = highlight(out, PythonLexer(), Terminal256Formatter(style="friendly"))
            except ImportError:
                pass
        return out.strip()

    def __str__(self):
        return self.format()

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
            out.append(f"<pre><code>{self}</code></pre>")
        return "\n".join(out)
