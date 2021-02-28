from textwrap import dedent

from IPython.testing.globalipapp import get_ipython
import pytest

from reprexlite import reprex


@pytest.fixture(scope="module")
def ipython():
    ipython = get_ipython()
    ipython.magic("load_ext reprexlite")
    return ipython


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
