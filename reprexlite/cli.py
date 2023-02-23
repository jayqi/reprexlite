from enum import Enum
from pathlib import Path
from typing import Optional

import typer

from reprexlite.config import ParsingMethod, ReprexConfig
from reprexlite.exceptions import InputSyntaxError, IPythonNotFoundError
from reprexlite.formatting import formatter_registry
from reprexlite.reprexes import Reprex
from reprexlite.version import __version__

app = typer.Typer()


def version_callback(version: bool):
    """Print reprexlite version to console."""
    if version:
        print(__version__)
        raise typer.Exit()


Venue = Enum(  # type: ignore
    "Venue", names={v.upper(): v for v in formatter_registry.keys()}, type=str
)
Venue.__doc__ = """Enum for valid venue options."""


def get_help(key: str):
    return ReprexConfig.get_help(key).replace("_", "-")


@app.command()
def main(
    editor: Optional[str] = typer.Option(
        None,
        "--editor",
        "-e",
        help=(
            "Specify editor to open in. Can be full path to executable or name to be searched on "
            "system search path. If None, will use Click's automatic editor detection. This will "
            "typically use the editor set to environment variable VISUAL or EDITOR. If value is "
            "'ipython' and IPython is installed, this will launch the interactive IPython editor "
            "where all cells are automatically run through reprexlite."
        ),
    ),
    infile: Optional[Path] = typer.Option(
        None,
        "--infile",
        "-i",
        help="Read code from an input file instead of entering in an editor.",
    ),
    outfile: Optional[Path] = typer.Option(
        None, "--outfile", "-o", help="Write output to file instead of printing to console."
    ),
    # Formatting
    venue: Venue = typer.Option(
        "gh",
        "--venue",
        "-v",
        help=get_help("venue"),
    ),
    advertise: Optional[bool] = typer.Option(
        None,
        "--advertise/--no-advertise",
        help=get_help("advertise"),
        is_flag=False,
        show_default=False,
    ),
    session_info: bool = typer.Option(False, help=get_help("session_info")),
    style: bool = typer.Option(False, help=get_help("style")),
    prompt: str = typer.Option("", help=get_help("prompt")),
    continuation: str = typer.Option("", help=get_help("continuation")),
    comment: str = typer.Option("#>", help=get_help("comment")),
    keep_old_results: bool = typer.Option(False, help=get_help("keep_old_results")),
    # Parsing
    parsing_method: ParsingMethod = typer.Option("auto", help=get_help("parsing_method")),
    input_prompt: Optional[str] = typer.Option(None, help=get_help("input_prompt")),
    input_continuation: Optional[str] = typer.Option(None, help=get_help("input_continuation")),
    input_comment: Optional[str] = typer.Option(None, help=get_help("input_comment")),
    verbose: Optional[bool] = typer.Option(None, "--verbose"),
    # Callbacks
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show reprexlite version and exit.",
    ),
):
    """Render reproducible examples of Python code for sharing. Your code will be executed and, in
    the default output style, the results will be embedded as comments below their associated
    lines.

    By default, your system's default command-line text editor will open for you to type or paste
    in your code. This editor can be changed by setting the VISUAL or EDITOR environment variable,
    or by explicitly passing in the --editor program. You can instead specify an input file with
    the --infile / -i option. If IPython is installed, an interactive IPython editor can also be
    launched using the --ipython flag.

    Additional markup will be added that is appropriate to the choice of venue formatting. For
    example, for the default `gh` venue for GitHub Flavored Markdown, the final reprex output will
    look like:

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
    <sup>Created at 2021-02-27 00:13:55 PST by [reprexlite](https://github.com/jayqi/reprexlite) v{version}</sup>
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
    """  # noqa: E501

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

    if editor and editor.lower() == "ipython":
        try:
            from reprexlite.ipython import ReprexTerminalIPythonApp
        except IPythonNotFoundError:
            print(
                "IPythonNotFoundError: ipython is required to be installed to use the IPython "
                "interactive editor."
            )
            raise typer.Exit(code=1)
        ReprexTerminalIPythonApp.set_reprex_config(config)
        ReprexTerminalIPythonApp.launch_instance(argv=[])
        raise typer.Exit()
    elif infile:
        with infile.open("r") as fp:
            input = fp.read()
    else:
        input = typer.edit(editor=editor) or ""

    if verbose:
        typer.echo(config)

    try:
        r = Reprex.from_input(input=input, config=config)
    except InputSyntaxError as e:
        print("ERROR: reprexlite has encountered an error while evaluating your input.")
        print(e)
        raise typer.Exit(1) from e

    if outfile:
        with outfile.open("w") as fp:
            fp.write(r.format(terminal=False))
        print(f"Wrote rendered reprex to {outfile}")
    else:
        print(r.format(terminal=True), end="")

    return r


if main.__doc__:
    main.__doc__ = main.__doc__.format(version=__version__)
