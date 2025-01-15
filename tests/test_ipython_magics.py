import builtins
import importlib
import sys
from textwrap import dedent

from IPython.terminal.interactiveshell import TerminalInteractiveShell
from IPython.testing import globalipapp
import pytest

from reprexlite.config import ReprexConfig
from reprexlite.reprexes import Reprex


@pytest.fixture()
def ipython(monkeypatch):
    monkeypatch.setattr(TerminalInteractiveShell, "_instance", None)
    ipython = globalipapp.start_ipython()
    ipython.run_line_magic("load_ext", "reprexlite")
    yield ipython
    ipython.run_cell("exit")
    del globalipapp.start_ipython.already_called


@pytest.fixture()
def no_ipython(monkeypatch):
    import_orig = builtins.__import__

    def mocked_import(name, *args):
        if name.startswith("IPython"):
            raise ModuleNotFoundError(name="IPython")
        return import_orig(name, *args)

    monkeypatch.setattr(builtins, "__import__", mocked_import)


def test_line_magic(ipython, capsys):
    ipython.run_line_magic("reprex", line="")
    captured = capsys.readouterr()
    print(captured.out)
    assert r"Cell Magic Usage: %%reprex" in captured.out


def test_cell_magic(ipython, capsys):
    input = dedent(
        """\
        x = 2
        x + 2
        """
    )
    ipython.run_cell_magic("reprex", line="--no-advertise --session-info", cell=input)
    captured = capsys.readouterr()

    r = Reprex.from_input(input, config=ReprexConfig(advertise=False, session_info=True))
    expected = r.render(terminal=True)

    print("\n---EXPECTED---\n")
    print(expected)
    print("\n---ACTUAL-----\n")
    print(captured.out)
    print("\n--------------\n")

    assert captured.out == expected


def test_no_ipython(no_ipython, monkeypatch):
    """Tests that not having ipython installed should not cause any import errors."""
    monkeypatch.delitem(sys.modules, "reprexlite")
    monkeypatch.delitem(sys.modules, "reprexlite.ipython")
    importlib.import_module("reprexlite")
