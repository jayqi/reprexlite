from contextlib import contextmanager
import re
from typing import Optional

from typer.testing import CliRunner

import reprexlite.cli
from reprexlite.config import ReprexConfig
from reprexlite.exceptions import IPythonNotFoundError
from reprexlite.reprexes import Reprex
from reprexlite.version import __version__

try:
    from IPython import InteractiveShell
    from IPython.core.magic import Magics, line_cell_magic, magics_class
    from IPython.core.release import version as ipython_version
    from IPython.core.usage import default_banner_parts
    from IPython.terminal.interactiveshell import TerminalInteractiveShell
    from IPython.terminal.ipapp import TerminalIPythonApp
except ModuleNotFoundError as e:
    if e.name == "IPython":
        raise IPythonNotFoundError(*e.args, name="IPython")
    else:
        raise  # pragma: no cover


runner = CliRunner()


@contextmanager
def patch_edit(input: str):
    """Patches typer.edit to return the input string instead of opening up the text editor. This
    is a trick to hook up the IPython cell magic's cell contents to the typer CLI app.
    """

    def return_input(*args, **kwargs) -> str:
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
            help_text = runner.invoke(reprexlite.cli.app, ["--help"]).stdout.strip()
            help_text = re.sub(r"^Usage: main", r"Cell Magic Usage: %%reprex", help_text)
            print(f"reprexlite v{__version__} IPython Magic\n\n" + help_text)
            return
        # Cell magic, render reprex
        with patch_edit(cell):
            result = runner.invoke(reprexlite.cli.app, line.split())
            print(result.stdout, end="")


def load_ipython_extension(ipython: InteractiveShell):
    """Special function to register this module as an IPython extension.
    https://ipython.readthedocs.io/en/stable/config/extensions/#writing-extensions
    """

    ipython.register_magics(ReprexMagics)


ipython_banner_parts = [
    default_banner_parts[0],
    f"reprexlite {__version__} -- Interactive reprex editor via IPython {ipython_version}.",
]


class ReprexTerminalInteractiveShell(TerminalInteractiveShell):
    """Subclass of IPython's TerminalInteractiveShell that automatically executes all cells using
    reprexlite instead of normally."""

    banner1 = "".join(ipython_banner_parts)
    _reprex_config: Optional[ReprexConfig] = None

    def run_cell(self, raw_cell: str, *args, **kwargs):
        # "exit()" and Ctrl+D short-circuit this and don't need to be handled
        if raw_cell != "exit":
            try:
                r = Reprex.from_input(raw_cell, config=self.reprex_config)
                r.print(end="")
            except Exception as e:
                print("ERROR: reprexlite has encountered an error while evaluating your input.")
                print(e, end="")

            # Store history
            self.history_manager.store_inputs(self.execution_count, raw_cell, raw_cell)
            self.execution_count += 1

            return None
        else:
            return super().run_cell(raw_cell, *args, **kwargs)

    @property
    def reprex_config(self) -> ReprexConfig:
        if self._reprex_config is None:
            self._reprex_config = ReprexConfig()
        return self._reprex_config


class ReprexTerminalIPythonApp(TerminalIPythonApp):
    """Subclass of TerminalIPythonApp that launches ReprexTerminalInteractiveShell."""

    interactive_shell_class = ReprexTerminalInteractiveShell

    @classmethod
    def set_reprex_config(cls, config: ReprexConfig):
        """Set the reprex config bound on the interactive shell."""
        cls.interactive_shell_class._reprex_config = config
