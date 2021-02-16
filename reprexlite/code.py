from itertools import chain
from pprint import pformat
from typing import Any, List, Union

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

    def __init__(self, result: Any, comment: str = "#>"):
        self.result = result
        self.comment = comment

    def __str__(self) -> str:
        if not self:
            return ""
        lines = pformat(self.result, indent=2, width=77).split("\n")
        return "\n".join(f"{self.comment} " + line for line in lines)

    def __bool__(self) -> bool:
        return self.result is not NO_RETURN


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
        try:
            return Result(eval(str(self), scope, scope))
        except SyntaxError:
            exec(str(self), scope, scope)
            return Result(NO_RETURN)

    def __str__(self) -> str:
        code = cst.Module(body=[self.stmt]).code.strip()
        if self.style:
            try:
                from black import format_str, Mode
            except ImportError:
                raise ImportError("Must install black to restyle code.")

            code = format_str(code, mode=Mode()).strip()
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

    def __init__(self, input: str, style: bool = False, comment: str = "#>", terminal=False):
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
                from pygments.lexers import PythonLexer
                from pygments.formatters import Terminal256Formatter

                out = highlight(out, PythonLexer(), Terminal256Formatter())
            except ImportError:
                pass
        return out.strip()

    def _repr_html_(self):
        out = []
        try:
            from pygments import highlight
            from pygments.lexers import PythonLexer
            from pygments.formatters import HtmlFormatter

            formatter = HtmlFormatter()
            out.append(f"<style>{formatter.get_style_defs('.highlight')}</style>")
            out.append(highlight(str(self.code_block), PythonLexer(), formatter))
        except ImportError:
            out.append(f"<pre><code>{self.code_block}</code></pre>")
        return "\n".join(out)
