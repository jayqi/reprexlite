from contextlib import contextmanager
import re
from typing import Optional

from IPython.core.magic import register_line_cell_magic
from typer.testing import CliRunner

import reprexlite.cli
from reprexlite.version import __version__

runner = CliRunner()


@contextmanager
def patch_edit(input: str):
    """Patches typer.edit to return the input string instead of opening up the text editor. This
    is a trick to hook up the IPython cell magic's cell contents to the typer CLI app.
    """

    def return_input() -> str:
        return input

    original = reprexlite.cli.typer.edit
    setattr(reprexlite.cli.typer, "edit", return_input)
    yield
    setattr(reprexlite.cli.typer, "edit", original)


@register_line_cell_magic
def reprex(line: str, cell: Optional[str] = None):
    """reprex IPython magic. Use line magic %reprex to print help. Use cell magic %%reprex to
    render a reprex."""
    # Line magic, print help
    if cell is None:
        help_text = runner.invoke(reprexlite.cli.app, ["--help"]).stdout
        help_text = re.sub(r"^Usage: main", r"Cell Magic Usage: %%reprex", help_text)
        help_text = re.sub(
            r"^  By default.+--infile / -i option\n\n",
            "",
            help_text,
            flags=re.MULTILINE | re.DOTALL,
        )
        help_text = re.sub(
            r"^  --version.*$",
            "",
            help_text,
            flags=re.MULTILINE | re.DOTALL,
        )
        print(f"reprexlite v{__version__} IPython Magic\n\n" + help_text.strip() + "\n")
        return
    # Cell magic, render reprex
    with patch_edit(cell):
        result = runner.invoke(reprexlite.cli.app, line.split())
        print(result.stdout.strip() + "\n")
