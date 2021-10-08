from pathlib import Path
from typing import Optional

from reprexlite.code import (
    DEFAULT_COMMENT,
    DEFAULT_CONTINUATION,
    DEFAULT_PROMPT,
    CodeBlock,
)
from reprexlite.formatting import Reprex, venues_dispatcher


def removeprefix(s: str, prefix: str):
    if s.startswith(prefix):
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
    lines = input.split("\n")
    code = ""
    for line in lines:
        if prompt and line.startswith(prompt + " "):
            code += removeprefix(line, prompt + " ") + "\n"
        elif continuation and line.startswith(continuation + " "):
            code += removeprefix(line, continuation + " ") + "\n"
        elif (comment and line.startswith(comment + " ")) or (prompt and continuation):
            if keep_old_results:
                code += "#" + line + "\n"
            else:
                continue
        else:
            code += line + "\n"
    return code


def reprex(
    input: str,
    outfile: Optional[Path] = None,
    venue="gh",
    advertise: Optional[bool] = None,
    session_info: bool = False,
    style: bool = False,
    prompt: str = DEFAULT_PROMPT,
    continuation: str = DEFAULT_CONTINUATION,
    comment: str = DEFAULT_COMMENT,
    input_prompt: Optional[str] = None,
    input_continuation: Optional[str] = None,
    input_comment: Optional[str] = None,
    keep_old_results: bool = False,
    print_=True,
    terminal=False,
) -> Reprex:
    """Render reproducible examples of Python code for sharing. This function will evaluate your
    code and returns an instance of a [`Reprex`][reprexlite.formatting.Reprex] subclass. Calling
    `str(...)` on the `Reprex` object will return your code with the evaluated results embedded
    as comments, plus additional markup appropriate to the sharing venue set by the `venue` keyword
    argument.

    For example, for the `gh` venue for GitHub Flavored Markdown, you'll get a reprex whose string
    representation looks like:

    ````
    ```python
    x = 2
    x + 2
    #> 4
    ```

    <sup>Created at 2021-02-15 16:58:47 PST by [reprexlite](https://github.com/jayqi/reprexlite) v0.1.0</sup>
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
        input (str): Block of Python code
        outfile (Optional[Path]): Optional file path to write reprex to. Defaults to None.
        venue (str): Determines the output format by the venue you want to share the code. Defaults
            to "gh" for GitHub Flavored Markdown.
        advertise (Optional[bool]): Whether to include a note that links back to the reprexlite
            package. Default `None` will use the default set by choice of `venue`.
        session_info (bool): Whether to include additional details about your Python version,
            operating system, and installed packages. Defaults to False.
        style (bool): Whether to autoformat your code with black. Defaults to False.
        comment (str): Line prefix to use for displaying evaluated results. Defaults to "#>".
        old_results (bool): Whether to keep old results, i.e., comment lines in input that match
            the `comment` prefix. False means these lines are removed, in effect meaning an
            inputted regex will have its results regenerated. Defaults to False.
        print_ (bool): Whether to print your reprex to console. Defaults to True.
        terminal (bool): Whether to use syntax highlighting for 256-color terminal display.
            Requires optional dependency Pygments. Defaults to False.

    Returns:
        Instance of a `Reprex` concrete subclass for `venue`.
    """

    if outfile or venue in ["html", "rtf"]:
        # Don't screw output file or lexing for HTML and RTF with terminal syntax highlighting
        terminal = False

    if input_prompt or input_continuation or input_comment:
        # User specified custom prefixes
        code = parse_input_to_code(
            input=input,
            prompt=prompt,
            continuation=continuation,
            comment=comment,
            keep_old_results=keep_old_results,
        )
    elif any(line.startswith(">>>") for line in input.split("\n")):
        # Check if doctest format
        code = parse_input_to_code(
            input=input, prompt=">>>", continuation="...", keep_old_results=keep_old_results
        )
    else:
        # Assume reprex format
        code = parse_input_to_code(
            input=input, comment=DEFAULT_COMMENT, keep_old_results=keep_old_results
        )

    code_block = CodeBlock.parse_and_evaluate(code)
    output = code_block.format(
        style=style, prompt=prompt, continuation=continuation, comment=comment, terminal=terminal
    )

    reprex = venues_dispatcher[venue](
        code_block=output, advertise=advertise, session_info=session_info
    )
    if outfile is not None:
        with outfile.open("w") as fp:
            fp.write(str(reprex) + "\n")
    if print_:
        print(reprex)
    return reprex
