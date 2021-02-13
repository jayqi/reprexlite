from itertools import chain
from pprint import pformat
from typing import Any, List, Optional, Union

import libcst as cst

from reprexlite.venues import venues_dispatcher, html

NO_RETURN = object()


class Result:
    def __init__(self, result: Any):
        self.result = result

    def format(self) -> str:
        if not self:
            return ""
        lines = pformat(self.result, indent=2, width=77).split("\n")
        return "\n".join("#> " + line for line in lines)

    def __str__(self) -> str:
        return self.format()

    def __bool__(self) -> bool:
        return self.result is not NO_RETURN


class Statement:
    def __init__(
        self, stmt: Union[cst.SimpleStatementLine, cst.BaseCompoundStatement], black: bool = False
    ):
        self.stmt = stmt
        self.black = black

    def as_code(self) -> str:
        code = cst.Module(body=[self.stmt]).code.strip()
        if self.black:
            try:
                from black import format_str, Mode
            except ImportError:
                raise ImportError("Must install black to use black formatting.")

            code = format_str(code, mode=Mode())
        return code

    def evaluate(self, scope: dict) -> Result:
        try:
            return Result(eval(self.as_code(), scope, scope))
        except SyntaxError:
            exec(self.as_code(), scope, scope)
            return Result(NO_RETURN)

    def __str__(self) -> str:
        return self.as_code()


class Reprex:
    def __init__(self, input: str, black: bool = False):
        self.input: str = input
        self.tree: cst.Module = cst.parse_module(input)
        self.statements: List[Statement] = [
            Statement(stmt, black=black) for stmt in self.tree.body
        ]
        self.namespace: dict = {}
        self.results: List[Result] = [stmt.evaluate(self.namespace) for stmt in self.statements]

    def __str__(self):
        return "\n".join(
            str(line) for line in chain.from_iterable(zip(self.statements, self.results)) if line
        )

    def _repr_html_(self):
        return html(self)


def reprex(input: str, venue="gh", black: bool = False, print_=True) -> Optional[str]:
    formatter = venues_dispatcher[venue]
    out = formatter(Reprex(input, black=black)) + "\n"
    if print_:
        print(out)
    return out
