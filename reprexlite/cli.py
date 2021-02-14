from functools import partial
from pathlib import Path
from typing import Optional

import typer

from reprexlite.reprex import Reprex
from reprexlite.venues import display_terminal, Venue, venues_dispatcher
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
        "If unspecified, will depend on default for each venue.",
    ),
    session_info: Optional[bool] = typer.Option(
        None,
        "--session-info",
        help="Whether to include details about session and installed packages.",
    ),
    style: Optional[bool] = typer.Option(
        None, "--style", help="Autoformat code with black. Requires black to be installed."
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
    results will be embedded as comments their associated lines. By default, your system's default
    command-line text editor will open for you to type or paste in your code. This editor can be
    changed by setting the EDITOR environment variable."""
    if infile:
        with infile.open("r") as fp:
            input = fp.read()
    else:
        input = typer.edit()
        if input is None:
            input = ""

    reprex = Reprex(input, style=style if style else False)
    formatter = partial(
        venues_dispatcher[venue.value], session_info=session_info if session_info else False
    )

    if outfile:
        with outfile.open("w") as fp:
            fp.write(formatter(reprex) + "\n")
        typer.echo(f"Wrote reprex to {outfile}")
    else:
        typer.echo(formatter(display_terminal(reprex)) + "\n")
