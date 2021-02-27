from pathlib import Path
from typing import Optional

import typer

from reprexlite.formatting import Venue
from reprexlite.reprex import reprex
from reprexlite.version import __version__

app = typer.Typer()


def version_callback(version: bool):
    """Print reprexlite version to console."""
    if version:
        typer.echo(__version__)
        raise typer.Exit()


@app.command()
def main(
    infile: Optional[Path] = typer.Option(
        None, "--infile", "-i", help="Read code from an input file instead via editor."
    ),
    outfile: Optional[Path] = typer.Option(
        None, "--outfile", "-o", help="Write output to file instead of printing to console."
    ),
    venue: Venue = typer.Option(
        "gh",
        "--venue",
        "-v",
        help="Output format appropriate to the venue where you plan to share this code.",
    ),
    advertise: Optional[bool] = typer.Option(
        None,
        help="Whether to include footer that credits reprexlite. "
        "If unspecified, will depend on specified venue's default.",
    ),
    session_info: Optional[bool] = typer.Option(
        None,
        "--session-info",
        help="Whether to include details about session and installed packages.",
    ),
    style: Optional[bool] = typer.Option(
        None, "--style", help="Autoformat code with black. Requires black to be installed."
    ),
    comment: str = typer.Option(
        "#>", "--comment", help="Comment prefix to use for results returned by expressions."
    ),
    old_results: Optional[bool] = typer.Option(
        None,
        "--old-results",
        help=(
            "Keep old results, i.e., lines that match the prefix specified by the --comment "
            "option. If not using this option, then such lines are removed, meaning that an input "
            "that is a reprex will be effectively regenerated."
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
        input = typer.edit()
        if input is None:
            input = ""

    rendered = reprex(
        input,
        outfile=outfile,
        venue=venue.value,
        advertise=advertise,
        session_info=session_info if session_info else False,
        style=style if style else False,
        comment=comment,
        old_results=old_results if old_results else False,
        print_=False,
        terminal=True,
    )

    if outfile:
        typer.echo(f"Wrote reprex to {outfile}")
    else:
        typer.echo(str(rendered) + "\n")
