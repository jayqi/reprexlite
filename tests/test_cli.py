from typer.testing import CliRunner

from reprexlite.cli import app
from reprexlite.version import __version__


runner = CliRunner()


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
