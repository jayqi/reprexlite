import builtins
import subprocess
from textwrap import dedent

import pytest
import typer
from typer.testing import CliRunner

from reprexlite.cli import app
from reprexlite.exceptions import IPythonNotFoundError
from reprexlite.version import __version__
from tests.utils import remove_ansi_escape

runner = CliRunner()

INPUT = dedent(
    """\
    x = 2
    x + 2
    """
)
EXPECTED = dedent(
    """\
    x = 2
    x + 2
    #> 4
    """
)


@pytest.fixture
def patch_edit(monkeypatch):
    class EditPatch:
        def __init__(self):
            self.input = INPUT

        def mock_edit(self, *args, **kwargs):
            return self.input

    patch = EditPatch()
    monkeypatch.setattr(typer, "edit", patch.mock_edit)
    return patch


@pytest.fixture
def no_ipython(monkeypatch):
    import_orig = builtins.__import__

    def mocked_import(name, *args):
        if name.startswith("reprexlite.ipython"):
            raise IPythonNotFoundError
        return import_orig(name, *args)

    monkeypatch.setattr(builtins, "__import__", mocked_import)


def test_reprex(patch_edit):
    result = runner.invoke(app)
    print(result.stdout)
    assert result.exit_code == 0
    assert EXPECTED in remove_ansi_escape(result.stdout)


def test_reprex_infile(tmp_path):
    infile = tmp_path / "infile.py"
    with infile.open("w") as fp:
        fp.write(INPUT)
    result = runner.invoke(app, ["-i", str(infile)])
    assert result.exit_code == 0
    assert EXPECTED in remove_ansi_escape(result.stdout)


def test_reprex_outfile(patch_edit, tmp_path):
    outfile = tmp_path / "outfile.md"
    result = runner.invoke(app, ["-o", str(outfile)])
    assert result.exit_code == 0
    with outfile.open("r") as fp:
        assert EXPECTED in fp.read()
    assert str(outfile) in result.stdout


def test_old_results(patch_edit):
    patch_edit.input = dedent(
        """\
        arr = [1, 2, 3, 4, 5]
        [x + 1 for x in arr]
        #> old line
        """
    )

    # no --old-results (default)
    result = runner.invoke(app)
    print(result.stdout)
    assert result.exit_code == 0
    assert "#> old line" not in result.stdout
    assert "#> [2, 3, 4, 5, 6]" in result.stdout

    # with --old-results
    result = runner.invoke(app, ["--keep-old-results"])
    print(result.stdout)
    assert result.exit_code == 0
    assert "#> old line" in result.stdout
    assert "#> [2, 3, 4, 5, 6]" in result.stdout


def test_ipython_editor():
    """Test that IPython interactive editor opens as expected. Not testing a reprex. Not sure how
    to inject input into the IPython shell."""
    result = runner.invoke(app, ["-e", "ipython"])
    assert result.exit_code == 0
    assert "Interactive reprex editor via IPython" in result.stdout  # text from banner


def test_ipython_editor_not_installed(no_ipython):
    """Test for expected error when opening the IPython interactive editor without IPython
    installed"""
    result = runner.invoke(app, ["-e", "ipython"])
    assert result.exit_code == 1
    assert "ipython is required" in result.stdout


def test_help():
    """Test the CLI with --help flag."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Render reproducible examples of Python code for sharing." in result.output


def test_version():
    """Test the CLI with --version flag."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert result.output.strip() == __version__


def test_python_m_version():
    """Test the CLI with python -m and --version flag."""
    result = subprocess.run(
        ["python", "-m", "reprexlite", "--version"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == __version__
