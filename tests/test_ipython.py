from textwrap import dedent

from IPython.terminal.interactiveshell import TerminalInteractiveShell
from IPython.testing import globalipapp
import pytest

from reprexlite import reprex


@pytest.fixture()
def ipython(monkeypatch):
    monkeypatch.setattr(TerminalInteractiveShell, "_instance", None)
    ipython = globalipapp.start_ipython()
    ipython.magic("load_ext reprexlite")
    yield ipython
    ipython.run_cell("exit")
    del globalipapp.start_ipython.already_called


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
    print(captured.out)
    expected = str(reprex(input, advertise=False, session_info=True, print_=False))
    assert captured.out == expected + "\n\n"
