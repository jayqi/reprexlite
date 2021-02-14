from functools import partial
from itertools import chain
from pathlib import Path
from pprint import pformat
from typing import Any, List, Optional, Union

import libcst as cst

from reprexlite.venues import venues_dispatcher, html


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

            code = format_str(code, mode=Mode())
        return code


class Reprex:
    """Class that takes Python code input and renders as a reprex output."""

    def __init__(self, input: str, style: bool = False, comment: str = "#>"):
        self.input: str = input
        self.tree: cst.Module = cst.parse_module(input)
        self.statements: List[Statement] = [
            Statement(stmt, style=style) for stmt in self.tree.body
        ]
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
        return "\n".join([header, code, footer]).strip()

    def _repr_html_(self):
        return html(self)

    def set_style(self, style: bool):
        for stmt in self.statements:
            stmt.style = style

    def set_comment(self, comment: str):
        for result in self.results:
            result.comment = comment


def reprex(
    input: str,
    outfile: Optional[Path] = None,
    venue="gh",
    advertise: Optional[bool] = None,
    session_info: bool = False,
    style: bool = False,
    comment: str = "#>",
    print_=True,
) -> Optional[str]:
    reprex = Reprex(input, style=style, comment=comment)
    formatter = venues_dispatcher[venue]
    if advertise is not None:
        formatter = partial(formatter, advertise=advertise)
    out = formatter(str(reprex), session_info=session_info) + "\n"
    if outfile is not None:
        with outfile.open("w") as fp:
            fp.write(out)
        return
    if print_:
        print(out)
        return
    return out
