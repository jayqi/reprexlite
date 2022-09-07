from enum import Enum
from pathlib import Path
from typing import Optional

import typer

from reprexlite.config import ParsingMethod, ReprexConfig
from reprexlite.formatting import venues_dispatcher
from reprexlite.reprexes import Reprex
from reprexlite.version import __version__

app = typer.Typer()


def version_callback(version: bool):
    """Print reprexlite version to console."""
    if version:
        print(__version__)
        raise typer.Exit()


def ipython_callback(ipython: bool):
    """Launch IPython-based interactive editor."""
    if ipython:
        try:
            from reprexlite.ipython import ReprexTerminalIPythonApp
        except ModuleNotFoundError:
            print("ipython is required to be installed to use IPython interactive editor.")
            raise typer.Exit(code=1)
        ReprexTerminalIPythonApp.launch_instance(argv=[])
        raise typer.Exit()


Venue = Enum("Venue", names={v.upper(): v for v in venues_dispatcher.keys()}, type=str)  # type: ignore
Venue.__doc__ = """Enum for valid venue options."""


@app.command()
def main(
    infile: Optional[Path] = typer.Option(
        None, "--infile", "-i", help="Read code from an input file instead via editor."
    ),
    outfile: Optional[Path] = typer.Option(
        None, "--outfile", "-o", help="Write output to file instead of printing to console."
    ),
    # Formatting
    venue: Venue = typer.Option(
        "gh",
        "--venue",
        "-v",
        help="",
    ),
    advertise: Optional[bool] = typer.Option(
        None,
        help="",
    ),
    session_info: Optional[bool] = typer.Option(
        None,
        "--session-info",
        help="",
    ),
    style: Optional[bool] = typer.Option(None, "--style", help=""),
    prompt: str = typer.Option("", help=""),
    continuation: str = typer.Option(
        "", help="Comment prefix to use for results returned by expressions."
    ),
    comment: str = typer.Option(
        "#>", help="Comment prefix to use for results returned by expressions."
    ),
    # Parsing
    parsing_method: ParsingMethod = "auto",
    input_prompt: Optional[str] = typer.Option(None),
    input_continuation: Optional[str] = typer.Option(None),
    input_comment: Optional[str] = typer.Option(None),
    keep_old_results: Optional[bool] = typer.Option(
        None,
        "--old-results",
        help=(
            "Keep old results, i.e., lines that match the prefix specified by the --comment "
            "option. If not using this option, then such lines are removed, meaning that an input "
            "that is a reprex will be effectively regenerated."
        ),
    ),
    # Callbacks
    ipython: Optional[bool] = typer.Option(
        None,
        "--ipython",
        callback=ipython_callback,
        is_eager=True,
        help=(
            "[experimental] Launch interactive IPython editor where all cells are automatically "
            "run as reprexes. Currently only supports default options. Requires IPython."
        ),
    ),
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show reprexlite version and exit.",
    ),
):
    """Render reproducible examples of Python code for sharing. Your code will be executed and the
    results will be embedded as comments below their associated lines.

    By default, your system's default command-line text editor will open for you to type or paste
    in your code. This editor can be changed by setting the EDITOR environment variable. You can
    instead specify an input file with the --infile / -i option

    Additional markup will be added that is appropriate to the choice of venue option. For example,
    for the default `gh` venue for GitHub Flavored Markdown, the final reprex will look like:

    \b
    ----------------------------------------
    ```python
    arr = [1, 2, 3, 4, 5]
    [x + 1 for x in arr]
    #> [2, 3, 4, 5, 6]
    max(arr) - min(arr)
    #> 4
    ```
    \b
    <sup>Created at 2021-02-27 00:13:55 PST by [reprexlite](https://github.com/jayqi/reprexlite) v0.3.1</sup>
    ----------------------------------------

    \b
    The supported venue formats are:
    \b
    - gh : GitHub Flavored Markdown
    - so : StackOverflow, alias for gh
    - ds : Discourse, alias for gh
    - html : HTML
    - py : Python script
    - rtf : Rich Text Format
    - slack : Slack
    """
    if infile:
        with infile.open("r") as fp:
            input = fp.read()
    else:
        input = typer.edit() or ""

    config = ReprexConfig(
        venue=venue.value,
        advertise=advertise,
        session_info=session_info or False,
        style=style or False,
        prompt=prompt,
        continuation=continuation,
        comment=comment,
        parsing_method=parsing_method.value,
        input_prompt=input_prompt,
        input_continuation=input_continuation,
        input_comment=input_comment,
        keep_old_results=keep_old_results or False,
    )

    reprex = Reprex.from_input(input=input, config=config)

    if outfile:
        with outfile.open("w") as fp:
            fp.write(reprex.format(terminal=False))
        print(f"Wrote reprex to {outfile}")
    else:
        print(reprex.format(terminal=True), end="")
