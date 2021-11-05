from typing import Optional

from reprexlite.code import DEFAULT_COMMENT, validate_prompts
from reprexlite.exceptions import InvalidInputPrefixes


def removeprefix(s: str, prefix: str):
    if s.startswith(prefix + " "):
        return s[len(prefix) + 1 :]
    elif s.startswith(prefix):
        return s[len(prefix) :]
    else:
        return s


def parse_input_to_code(
    input: str,
    prompt: Optional[str] = None,
    continuation: Optional[str] = None,
    comment: Optional[str] = None,
    keep_old_results: bool = False,
):
    if prompt or continuation or comment:
        # User specified custom prefixes
        return _parse(
            input=input,
            prompt=prompt,
            continuation=continuation,
            comment=comment,
            keep_old_results=keep_old_results,
        )
    elif any(line.startswith(">>>") for line in input.split("\n")):
        # Check if doctest format
        return _parse(
            input=input, prompt=">>>", continuation="...", keep_old_results=keep_old_results
        )
    else:
        # Assume reprex format
        return _parse(input=input, comment=DEFAULT_COMMENT, keep_old_results=keep_old_results)


def _parse(
    input: str,
    prompt: Optional[str] = None,
    continuation: Optional[str] = None,
    comment: Optional[str] = None,
    keep_old_results: bool = False,
):
    if not any([prompt, continuation, comment]):
        raise InvalidInputPrefixes(
            "Cannot parse input if all of prompt, continuation, and comment are blank."
        )
    lines = input.split("\n")
    out_lines = []
    for line in lines:
        if prompt and line.startswith(prompt):
            out_lines.append(removeprefix(line, prompt))
        elif continuation and line.startswith(continuation):
            out_lines.append(removeprefix(line, continuation))
        elif comment and line.startswith(comment):
            if keep_old_results:
                out_lines.append("# " + removeprefix(line, comment))
            else:
                continue
        elif prompt and continuation and line.strip():
            if keep_old_results:
                out_lines.append("# " + line)
            else:
                continue
        else:
            out_lines.append(line)
    return "\n".join(out_lines)
