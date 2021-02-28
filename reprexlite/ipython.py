from contextlib import contextmanager
import re
from typing import Optional

from IPython import InteractiveShell
from IPython.core.magic import Magics, line_cell_magic, magics_class
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


@magics_class
class ReprexMagics(Magics):
    @line_cell_magic
    def reprex(self, line: str, cell: Optional[str] = None):
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


def load_ipython_extension(ipython: InteractiveShell):
    """Special function to register this module as an IPython extension.
    https://ipython.readthedocs.io/en/stable/config/extensions/#writing-extensions
    """

    ipython.register_magics(ReprexMagics)
