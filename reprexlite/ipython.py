from contextlib import contextmanager
import re
from typing import Optional

from IPython import InteractiveShell
from IPython.core.magic import Magics, line_cell_magic, magics_class
from IPython.core.release import version as ipython_version
from IPython.core.usage import default_banner_parts
from IPython.terminal.interactiveshell import TerminalInteractiveShell
from IPython.terminal.ipapp import TerminalIPythonApp
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


ipython_banner_parts = default_banner_parts[:-1].copy()
ipython_banner_parts.append(
    f"reprexlite {__version__} -- Interactive reprex editor via IPython {ipython_version}."
)


class ReprexTerminalInteractiveShell(TerminalInteractiveShell):
    """Subclass of IPython's TerminalInteractiveShell that automatically runs all cells using the
    %%reprex cell magic."""

    banner1 = "".join(ipython_banner_parts)

    def run_cell(self, raw_cell, *args, **kwargs):
        if raw_cell != "exit":
            raw_cell = "%%reprex\n" + raw_cell
        super().run_cell(raw_cell, *args, **kwargs)

    def init_magics(self):
        super().init_magics()
        self.register_magics(ReprexMagics)


class ReprexTerminalIPythonApp(TerminalIPythonApp):
    """Subclass of TerminalIPythonApp that launches ReprexTerminalInteractiveShell."""

    interactive_shell_class = ReprexTerminalInteractiveShell
