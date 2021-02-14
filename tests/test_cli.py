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
def mock_edit(monkeypatch):
    def edit():
        return INPUT

    monkeypatch.setattr(typer, "edit", edit)


def test_reprex(mock_edit):
    result = runner.invoke(app)
    print(result.stdout)
    assert result.exit_code == 0
    assert EXPECTED in result.stdout


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
