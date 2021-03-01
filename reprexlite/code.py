from contextlib import redirect_stdout
from io import StringIO
from itertools import chain
from pprint import pformat
import traceback
from typing import Any, List, Optional, Union

import libcst as cst

NO_RETURN = object()
"""Explicit placeholder object for statements, which have no return value (as opposed to
expressions)."""


class Result:
    """Class that holds the result of evaluated code. Use `str(...)` on an instance to produce a
    pretty-formatted comment block representation of the result.

    Attributes:
        result (Any): Some Python object, intended to be the return value of evaluated Python code.
        comment (str): Line prefix to use when rendering the result for a reprex.
    """

    def __init__(self, result: Any, stdout: Optional[str] = None, comment: str = "#>"):
        self.result = result
        self.stdout = stdout
        self.comment = comment

    def __str__(self) -> str:
        lines = []
        if self.stdout:
            lines.extend(self.stdout.split("\n"))
        if self.result is not NO_RETURN and (self.result is not None or not self.stdout):
            # NO_RETURN -> don't print
            # None and stdout -> don't print
            # None and no stdout -> print
            # Anything else -> print
            lines.extend(pformat(self.result, indent=2, width=77).split("\n"))
        return "\n".join(f"{self.comment} " + line for line in lines)

    def __bool__(self) -> bool:
        # If result is NO_RETURN and blank stdout, nothing to print
        return self.result is not NO_RETURN or bool(self.stdout)


class Statement:
    """Class that holds a LibCST parsed statement. The evaluate method will evaluate the statement
    and return a [`Result`][reprexlite.code.Result] object. To recover the original source code
    for an instancement, call `str(...)` on it. You can optionally autoformat the returned source
    code, controlled by the `style` attribute.

    Attributes:
        stmt (Union[libcst.SimpleStatementLine, libcst.BaseCompoundStatement]): LibCST parsed
            statement.
        style (bool): Whether to autoformat the source code with black.
    """

    def __init__(
        self, stmt: Union[cst.SimpleStatementLine, cst.BaseCompoundStatement], style: bool = False
    ):
        self.stmt = stmt
        self.style = style

    def evaluate(self, scope: dict) -> Result:
        stdout_io = StringIO()
        try:
            with redirect_stdout(stdout_io):
                try:
                    result = eval(str(self).strip(), scope, scope)
                except SyntaxError:
                    exec(str(self).strip(), scope, scope)
                    result = NO_RETURN
            stdout = stdout_io.getvalue().strip()
        except Exception:
            result = NO_RETURN
            stdout = traceback.format_exc().strip()
        finally:
            stdout_io.close()
        return Result(result, stdout=stdout)

    def __str__(self) -> str:
        code = cst.Module(body=[self.stmt]).code
        if self.style:
            try:
                from black import Mode, format_str
            except ImportError:
                raise ImportError("Must install black to restyle code.")

            code = format_str(code, mode=Mode())
        if code.endswith("\n"):
            # Strip trailing newline without stripping deliberate ones.
            code = code[:-1]
        return code


class CodeBlock:
    """Class that takes a block of Python code input and evaluates it. Call `str(...)` on an
    instance to get back a string containing the original source with evaluated outputs embedded
    as comments below each statement.

    Attributes:
        input (str): Block of Python code
        style (bool): Whether to use black to autoformat code in returned string representation.
        comment (str): Line prefix to use when rendering the evaluated results.
        terminal (bool): Whether to apply syntax highlighting to the string representation.
            Requires optional dependency Pygments.
        tree (libcst.Module): Parsed LibCST concrete syntax tree of input code.
        statements (List[Statement]): List of individual statements parsed from input code.
        results (List[Result]): List of evaluated results corresponding to each item of statements.
    """

    def __init__(
        self,
        input: str,
        style: bool = False,
        comment: str = "#>",
        terminal=False,
        old_results: bool = False,
    ):
        """Initializer method.

        Args:
            input (str): Block of Python code
            style (bool): Whether to use black to autoformat code in returned string
                representation. Defaults to False.
            comment (str): Line prefix to use when rendering the evaluated results. Defaults to
                "#>".
            terminal (bool): Whether to apply syntax highlighting to the string representation.
                Requires optional dependency Pygments. Defaults to False.
            old_results (bool): Whether to keep old results, i.e., comment lines in input that
                match the `comment` prefix. False means these lines are removed, in effect meaning
                an inputted regex will have its results regenerated. Defaults to False.
        """
        if any(line.startswith(">>>") for line in input.split("\n")):
            input = repl_to_reprex_code(input, comment=comment)
        if not old_results and comment in input:
            input = "\n".join(line for line in input.split("\n") if not line.startswith(comment))
        self.input: str = input
        self.terminal = terminal
        # Parse code
        self.tree: cst.Module = cst.parse_module(input)
        self.statements: List[Statement] = [
            Statement(stmt, style=style) for stmt in self.tree.body
        ]
        # Evaluate code
        self.namespace: dict = {}
        self.results: List[Result] = [stmt.evaluate(self.namespace) for stmt in self.statements]
        for res in self.results:
            res.comment = comment

    def __str__(self):
        header = cst.Module(body=[], header=self.tree.header).code.strip()
        code = "\n".join(
            str(line) for line in chain.from_iterable(zip(self.statements, self.results)) if line
        )
        footer = cst.Module(body=[], footer=self.tree.footer).code.strip()
        out = "\n".join([header, code, footer])
        if self.terminal:
            try:
                from pygments import highlight
                from pygments.formatters import Terminal256Formatter
                from pygments.lexers import PythonLexer

                out = highlight(out, PythonLexer(), Terminal256Formatter(style="friendly"))
            except ImportError:
                pass
        return out.strip()

    def _repr_html_(self):
        out = []
        try:
            from pygments import highlight
            from pygments.formatters import HtmlFormatter
            from pygments.lexers import PythonLexer

            formatter = HtmlFormatter(style="friendly", wrapcode=True)
            out.append(f"<style>{formatter.get_style_defs('.highlight')}</style>")
            out.append(highlight(str(self), PythonLexer(), formatter))
        except ImportError:
            out.append(f"<pre><code>{self}</code></pre>")
        return "\n".join(out)


def repl_to_reprex_code(input: str, comment: str = "#>") -> str:
    """Reformat a code block copied from a Python REPL to a reprex-style code block.

    Args:
        input (str): code block
        comment (str): Line prefix to use when rendering the evaluated results. Defaults to "#>".

    Returns:
        Reformatted code block in reprex-style.
    """
    out = []
    for line in input.split("\n"):
        if line.startswith(">>>") or line.startswith("..."):
            out.append(line[4:])
        elif line.strip() == "":
            out.append(line)
        else:
            out.append(comment + " " + line)
    return "\n".join(out)
