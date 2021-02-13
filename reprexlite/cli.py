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
    infile: Optional[Path] = typer.Option(None, "--infile", "-i", help="Input filename."),
    outfile: Optional[Path] = typer.Option(None, "--outfile", "-o", help="Output filename."),
    venue: Venue = typer.Option("gh", "--venue", "-v", help="Format"),
    black: Optional[bool] = typer.Option(
        None, "--black", "-b", help="Format input code with black."
    ),
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show reprexlite version and exit.",
    ),
):
    """Reprex"""
    if infile:
        with infile.open("r") as fp:
            input = fp.read()
    else:
        input = typer.edit()

    reprex = Reprex(input, black=black if black else False)
    formatter = venues_dispatcher[venue.value]

    if outfile:
        with outfile.open("w") as fp:
            fp.write(formatter(reprex) + "\n")
        typer.echo(f"Wrote reprex to {outfile}")
    else:
        typer.echo(formatter(display_terminal(reprex)) + "\n")
