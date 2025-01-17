import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
from typing import Annotated, Optional

from cyclopts import App, Parameter

from reprexlite.config import ReprexConfig
from reprexlite.exceptions import (
    EditorError,
    InputSyntaxError,
    IPythonNotFoundError,
)
from reprexlite.reprexes import Reprex
from reprexlite.version import __version__


def get_version():
    return __version__


app = App(name="reprex", version=get_version, help_format="plaintext")


def launch_ipython(config: ReprexConfig):
    try:
        from reprexlite.ipython import ReprexTerminalIPythonApp
    except IPythonNotFoundError:
        print(
            "IPythonNotFoundError: ipython is required to be installed to use the IPython "
            "interactive editor."
        )
        sys.exit(1)
    ReprexTerminalIPythonApp.set_reprex_config(config)
    ReprexTerminalIPythonApp.launch_instance(argv=[])
    sys.exit(0)


def launch_editor(editor) -> str:
    fw, name = tempfile.mkstemp(prefix="reprexlite-", suffix=".py")
    try:
        os.close(fw)  # Close the file descriptor
        # Open editor and edit the file
        proc = subprocess.Popen(args=f"{editor} {name}", shell=True)
        exit_code = proc.wait()
        if exit_code != 0:
            raise EditorError(f"{editor}: Editing failed with exit code {exit_code}")

        # Read the file back in
        with open(name, "rb") as fp:
            content = fp.read()
        return content.decode("utf-8-sig").replace("\r\n", "\n")
    except OSError as e:
        raise EditorError(f"{editor}: Editing failed: {e}") from e
    finally:
        os.unlink(name)


def get_editor() -> str:
    """Determine an editor to use for editing code."""
    for key in "VISUAL", "EDITOR":
        env_val = os.environ.get(key)
        if env_val:
            return env_val
    if platform.system() == "Windows":
        return "notepad"
    for editor in ("sensible-editor", "vim", "nano"):
        if os.system(f"which {editor} >/dev/null 2>&1") == 0:
            return editor
    return "vi"


def handle_editor(config: ReprexConfig) -> str:
    """Determines what to do based on the editor configuration."""
    editor = config.editor or get_editor()
    if editor == "ipython":
        launch_ipython(config)
    else:
        return launch_editor(editor)


@app.default
def main(
    *,
    infile: Annotated[Optional[Path], Parameter(name=("--infile", "-i"))] = None,
    outfile: Annotated[Optional[Path], Parameter(name=("--outfile", "-o"))] = None,
    config: Annotated[ReprexConfig, Parameter(name="*")] = ReprexConfig(),
    verbose: bool = False,
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
    example, for the default 'gh' venue for GitHub Flavored Markdown, the final reprex output will
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

    if infile:
        with infile.open("r") as fp:
            input = fp.read()
    else:
        input = handle_editor(config)
        if input.strip() == "":
            print("No input provided or saved via the editor. Exiting.")
            sys.exit(0)

    if verbose:
        print(config)

    try:
        r = Reprex.from_input(input=input, config=config)
    except InputSyntaxError as e:
        print("ERROR: reprexlite has encountered an error while evaluating your input.")
        print(e)
        raise

    if outfile:
        with outfile.open("w") as fp:
            fp.write(r.render_and_format(terminal=False))
        print(f"Wrote rendered reprex to {outfile}")
    else:
        print(r.render_and_format(terminal=True), end="")

    return r


def entrypoint():
    """Entrypoint for the reprex command-line interface. This function is configured as the reprex
    entrypoint under [project.scripts].
    https://packaging.python.org/en/latest/specifications/entry-points/#use-for-scripts
    """
    app()
