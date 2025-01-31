import dataclasses
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
from typing import Annotated, Optional

from cyclopts import App, Parameter
import cyclopts.config
from platformdirs import user_config_dir

from reprexlite.config import ReprexConfig
from reprexlite.exceptions import (
    EditorError,
    InputSyntaxError,
    IPythonNotFoundError,
)
from reprexlite.formatting import formatter_registry
from reprexlite.reprexes import Reprex
from reprexlite.version import __version__


def get_version():
    return __version__


HELP_TEMPLATE = """
Render reproducible examples of Python code for sharing. Your code will be executed and, in
the default output style, the results will be embedded as comments below their associated
lines.

By default, your system's default command-line text editor will open for you to type or paste
in your code. This editor can be changed by setting either of the `VISUAL` or `EDITOR` environment
variables, or by explicitly passing in the --editor program. The interactive IPython editor
requires IPython to be installed. You can also instead specify an input file with the
--infile / -i option.

Additional markup will be added that is appropriate to the choice of venue formatting. For
example, for the default 'gh' venue for GitHub Flavored Markdown, the final reprex output will
look like:

````
```python
arr = [1, 2, 3, 4, 5]
[x + 1 for x in arr]
#> [2, 3, 4, 5, 6]
max(arr) - min(arr)
#> 4
```

<sup>Created at 2021-02-27 00:13 PST by [reprexlite](https://github.com/jayqi/reprexlite) v{version}</sup>
````

The supported venue formats are:
{venue_formats}
"""  # noqa: E501


def get_help():
    help_text = HELP_TEMPLATE.format(
        version=get_version(),
        venue_formats="\n".join(
            f"- {key.value} : {entry.label}" for key, entry in formatter_registry.items()
        ),
    )
    return help_text


pyproject_toml_loader = cyclopts.config.Toml(
    "pyproject.toml",
    root_keys=("tool", "reprexlite"),
    search_parents=True,
    use_commands_as_keys=False,
)

reprexlite_toml_loader = cyclopts.config.Toml(
    "reprexlite.toml",
    search_parents=True,
    use_commands_as_keys=False,
)

dot_reprexlite_toml_loader = cyclopts.config.Toml(
    ".reprexlite.toml",
    search_parents=True,
    use_commands_as_keys=False,
)


user_reprexlite_toml_loader = cyclopts.config.Toml(
    Path(user_config_dir(appname="reprexlite")) / "config.toml",
    search_parents=False,
    use_commands_as_keys=False,
)

app = App(
    name="reprex",
    version=get_version,
    help_format="markdown",
    help=get_help(),
    config=(
        pyproject_toml_loader,
        reprexlite_toml_loader,
        dot_reprexlite_toml_loader,
        user_reprexlite_toml_loader,
    ),
)


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
    infile: Annotated[
        Optional[Path],
        Parameter(
            name=("--infile", "-i"),
            help="Read code from this file instead of opening an editor.",
        ),
    ] = None,
    outfile: Annotated[
        Optional[Path],
        Parameter(
            name=("--outfile", "-o"),
            help="Write rendered reprex to this file instead of standard out.",
        ),
    ] = None,
    config: Annotated[ReprexConfig, Parameter(name="*")] = ReprexConfig(),
    verbose: Annotated[tuple[bool, ...], Parameter(name=("--verbose", "-V"))] = (),
    debug: Annotated[bool, Parameter(show=False)] = False,
):
    verbosity = sum(verbose)
    if verbosity:
        sys.stderr.write("infile: {}\n".format(infile))
        sys.stderr.write("outfile: {}\n".format(outfile))
        sys.stderr.write("config: {}\n".format(config))

    if debug:
        data = {"infile": infile, "outfile": outfile, "config": dataclasses.asdict(config)}
        sys.stdout.write(json.dumps(data))
        return data

    if infile:
        if verbose:
            sys.stderr.write(f"Reading from input file: {infile}")
        with infile.open("r") as fp:
            input = fp.read()
    else:
        input = handle_editor(config)
        if input.strip() == "":
            print("No input provided or saved via the editor. Exiting.")
            sys.exit(0)

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
