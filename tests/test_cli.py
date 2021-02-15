import subprocess
from textwrap import dedent

import pytest
import typer
from typer.testing import CliRunner

from reprexlite.cli import app
from reprexlite.version import __version__


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
    def mock_edit():
        return INPUT

    monkeypatch.setattr(typer, "edit", mock_edit)


def test_reprex(patch_edit):
    result = runner.invoke(app)
    print(result.stdout)
    assert result.exit_code == 0
    assert EXPECTED in result.stdout


def test_reprex_infile(tmp_path):
    infile = tmp_path / "infile.py"
    with infile.open("w") as fp:
        fp.write(INPUT)
    result = runner.invoke(app, ["-i", str(infile)])
    assert result.exit_code == 0
    assert EXPECTED in result.stdout


def test_reprex_outfile(patch_edit, tmp_path):
    outfile = tmp_path / "outfile.md"
    result = runner.invoke(app, ["-o", str(outfile)])
    assert result.exit_code == 0
    with outfile.open("r") as fp:
        assert EXPECTED in fp.read()
    assert str(outfile) in result.stdout


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
