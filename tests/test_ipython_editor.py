import builtins
import importlib
import sys
from textwrap import dedent

import pytest

from reprexlite.exceptions import IPythonNotFoundError
from reprexlite.reprexes import Reprex
from tests.utils import remove_ansi_escape, requires_ipython, requires_no_ipython


@pytest.fixture()
def reprexlite_ipython(monkeypatch):
    from IPython.testing import globalipapp

    from reprexlite.ipython import ReprexTerminalInteractiveShell

    monkeypatch.setattr(globalipapp, "TerminalInteractiveShell", ReprexTerminalInteractiveShell)
    monkeypatch.setattr(ReprexTerminalInteractiveShell, "_instance", None)
    ipython = globalipapp.start_ipython()
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


@pytest.fixture()
def ipython_bad_dependency(monkeypatch):
    module_name = "dependency_of_ipython"
    import_orig = builtins.__import__

    def mocked_import(name, *args):
        if name.startswith("IPython"):
            raise ModuleNotFoundError(name=module_name)
        return import_orig(name, *args)

    monkeypatch.setattr(builtins, "__import__", mocked_import)
    yield module_name


@requires_ipython
def test_ipython_editor(reprexlite_ipython, capsys):
    input = dedent(
        """\
        x = 2
        x + 2
        """
    )
    reprexlite_ipython.run_cell(input)
    captured = capsys.readouterr()
    r = Reprex.from_input(input)
    expected = r.format()

    print("\n---EXPECTED---\n")
    print(expected)
    print("\n---ACTUAL-----\n")
    print(captured.out)
    print("\n--------------\n")
    assert remove_ansi_escape(captured.out) == expected


@requires_no_ipython
def test_no_ipython_error(monkeypatch):
    with pytest.raises(IPythonNotFoundError):
        importlib.import_module("reprexlite.ipython")


@requires_ipython
def test_bad_ipython_dependency(ipython_bad_dependency, monkeypatch):
    """Test that a bad import inside IPython does not trigger IPythonNotFoundError"""
    monkeypatch.delitem(sys.modules, "reprexlite.ipython")
    with pytest.raises(ModuleNotFoundError) as exc_info:
        importlib.import_module("reprexlite.ipython")
    assert not isinstance(exc_info.type, IPythonNotFoundError)
    assert exc_info.value.name != "IPython"
    assert exc_info.value.name == ipython_bad_dependency
