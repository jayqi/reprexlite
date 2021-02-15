from itertools import chain
from pprint import pformat
from typing import Any, List, Union

import libcst as cst


NO_RETURN = object()


class Result:
    """Class that holds the result of evaluated code and generates a pretty-formatted string
    represetation."""

    def __init__(self, result: Any, comment: str = "#>"):
        self.result = result

    def __str__(self) -> str:
        if not self:
            return ""
        lines = pformat(self.result, indent=2, width=77).split("\n")
        return "\n".join(f"{self.comment} " + line for line in lines)

    def __bool__(self) -> bool:
        return self.result is not NO_RETURN


class Statement:
    """Class that holds a LibCST parsed statement. It can evaluate it and return a Result, and it
    reproduces the source code as a string.
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
    """Class that takes Python code input and renders as a reprex output."""

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
