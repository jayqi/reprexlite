from enum import Enum
from typing import Iterator, Optional, Tuple

from reprexlite.exceptions import (
    InvalidInputPrefixesError,
    NoPrefixMatchError,
    PromptLengthMismatchError,
    UnexpectedError,
)


def removeprefix(s: str, prefix: str):
    if s.startswith(prefix + " "):
        return s[len(prefix) + 1 :]
    elif s.startswith(prefix):
        return s[len(prefix) :]
    else:
        raise UnexpectedError(  # pragma: nocover
            "removeprefix should not be called when not matching prefix. "
            "If you see this error under normal useage, please report at "
            "https://github.com/jayqi/reprexlite/issues"
        )


class LineType(Enum):
    CODE = "CODE"
    RESULT = "RESULT"


def parse(
    input: str,
    prompt: Optional[str],
    continuation: Optional[str],
    comment: Optional[str],
) -> Iterator[Tuple[str, LineType]]:
    if not any((prompt, continuation, comment)):
        raise InvalidInputPrefixesError(
            "Cannot parse input if all of prompt, continuation, and comment are blank."
        )
    if len(prompt or "") != len(continuation or ""):
        raise PromptLengthMismatchError(
            f"Primary prompt ('{prompt}') and continuation prompt ('{continuation}') must be "
            "equal lengths."
        )

    for line_no, line in enumerate(input.split("\n")):
        # Case 1: With Prompt/Continuation, no Comment (e.g., doctest style)
        if prompt and continuation and not comment:
            if line.startswith(prompt):
                yield removeprefix(line, prompt), LineType.CODE
            elif line.startswith(continuation):
                yield removeprefix(line, continuation), LineType.CODE
            elif line == "":
                yield line, LineType.CODE
            else:
                yield line, LineType.RESULT

        # Case 2: No Prompt or Continuation, with Comment (e.g., reprex style)
        elif not prompt and not continuation and comment:
            if line.startswith(comment):
                yield removeprefix(line, comment), LineType.RESULT
            else:
                yield line, LineType.CODE

        # Case 3: Both Prompt/Contiuation and Comment
        elif prompt and continuation and comment:
            if line.startswith(prompt):
                yield removeprefix(line, prompt), LineType.CODE
            elif line.startswith(continuation):
                yield removeprefix(line, continuation), LineType.CODE
            elif line.startswith(comment):
                yield removeprefix(line, comment), LineType.RESULT
            elif line == "":
                yield line, LineType.CODE
            else:
                raise NoPrefixMatchError(
                    f"Line {line_no+1} does not match any of prompt, continuation, or comment "
                    f"prefixes: '{line}'"
                )

        else:
            raise UnexpectedError(  # pragma: nocover
                "Unexpected case when using parse. If you see this error under normal useage, "
                "please report at https://github.com/jayqi/reprexlite/issues"
            )


def parse_reprex(input: str):
    return parse(input=input, prompt=None, continuation=None, comment="#>")


def parse_doctest(input: str):
    return parse(input=input, prompt=">>>", continuation="...", comment=None)


def auto_parse(input: str):
    if any(line.startswith(">>>") for line in input.split("\n")):
        yield from parse_doctest(input)
    else:
        yield from parse_reprex(input)
