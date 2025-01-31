import builtins
import importlib
import subprocess
import sys
from textwrap import dedent

import platformdirs
import pytest

import reprexlite.cli
from reprexlite.exceptions import IPythonNotFoundError
from reprexlite.version import __version__
from tests.utils import remove_ansi_escape

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
            sys.stderr.write("Mocking editor\n")
            return self.input

    patch = EditPatch()
    monkeypatch.setattr(reprexlite.cli, "handle_editor", patch.mock_edit)
    yield patch


@pytest.fixture
def no_ipython(monkeypatch):
    import_orig = builtins.__import__

    def mocked_import(name, *args):
        if name.startswith("reprexlite.ipython"):
            raise IPythonNotFoundError
        return import_orig(name, *args)

    monkeypatch.setattr(builtins, "__import__", mocked_import)


@pytest.fixture
def project_dir(tmp_path, monkeypatch):
    project_dir = tmp_path / "project_dir"
    project_dir.mkdir()
    monkeypatch.chdir(project_dir)
    importlib.reload(reprexlite.cli)
    yield project_dir


@pytest.fixture
def user_config_dir(tmp_path, monkeypatch):
    user_config_dir = tmp_path / "user_config_dir"
    user_config_dir.mkdir()

    def _mock_get_user_config_dir(*args, **kwargs):
        return user_config_dir

    monkeypatch.setattr(platformdirs, "user_config_dir", _mock_get_user_config_dir)
    importlib.reload(reprexlite.cli)
    yield user_config_dir


def test_reprex(project_dir, user_config_dir, patch_edit, capsys):
    assert reprexlite.cli.handle_editor == patch_edit.mock_edit
    capsys.readouterr()
    reprexlite.cli.app([])
    stdout = capsys.readouterr().out
    print(stdout)
    assert EXPECTED in remove_ansi_escape(stdout)


def test_reprex_infile(project_dir, user_config_dir, tmp_path, capsys):
    infile = tmp_path / "infile.py"
    with infile.open("w") as fp:
        fp.write(INPUT)
    reprexlite.cli.app(["-i", str(infile)])
    stdout = capsys.readouterr().out
    print(stdout)
    assert EXPECTED in remove_ansi_escape(stdout)


def test_reprex_outfile(project_dir, user_config_dir, patch_edit, tmp_path, capsys):
    outfile = tmp_path / "outfile.md"
    reprexlite.cli.app(["-o", str(outfile)])
    with outfile.open("r") as fp:
        assert EXPECTED in fp.read()
    stdout = capsys.readouterr().out
    print(stdout)
    assert str(outfile) in stdout


def test_old_results(project_dir, user_config_dir, patch_edit, capsys):
    patch_edit.input = dedent(
        """\
        arr = [1, 2, 3, 4, 5]
        [x + 1 for x in arr]
        #> old line
        """
    )

    # no --old-results (default)
    capsys.readouterr()
    reprexlite.cli.app([])
    stdout = capsys.readouterr().out
    print(stdout)
    assert "#> old line" not in stdout
    assert "#> [2, 3, 4, 5, 6]" in stdout

    # with --old-results
    reprexlite.cli.app(["--keep-old-results"])
    stdout = capsys.readouterr().out
    print(stdout)
    assert "#> old line" in stdout
    assert "#> [2, 3, 4, 5, 6]" in stdout


def test_ipython_editor(project_dir, user_config_dir):
    """Test that IPython interactive editor opens as expected. Not testing a reprex."""

    result = subprocess.run(
        [sys.executable, "-I", "-m", "reprexlite", "-e", "ipython"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        text=True,
        input="exit",
    )
    assert result.returncode == 0
    assert "Interactive reprex editor via IPython" in result.stdout  # text from banner


def test_ipython_editor_not_installed(project_dir, user_config_dir, no_ipython, capsys):
    """Test for expected error when opening the IPython interactive editor without IPython
    installed"""
    with pytest.raises(SystemExit) as excinfo:
        reprexlite.cli.app(["-e", "ipython"])
        assert excinfo.value.code == 1
    stdout = capsys.readouterr().out
    assert "ipython is required" in stdout


def test_help(project_dir, user_config_dir, capsys):
    """Test the CLI with --help flag."""
    reprexlite.cli.app(["--help"])
    stdout = capsys.readouterr().out
    assert "Render reproducible examples of Python code for sharing." in stdout


def test_version(project_dir, user_config_dir, capsys):
    """Test the CLI with --version flag."""
    reprexlite.cli.app(["--version"])
    stdout = capsys.readouterr().out
    assert stdout.strip() == __version__


def test_python_m_version(project_dir, user_config_dir):
    """Test the CLI with python -m and --version flag."""
    result = subprocess.run(
        [sys.executable, "-I", "-m", "reprexlite", "--version"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == __version__


def test_pyproject_toml(project_dir, user_config_dir):
    pyproject_toml = project_dir / "pyproject.toml"
    with pyproject_toml.open("w") as fp:
        fp.write(
            dedent(
                """\
                [tool.reprexlite]
                editor = "test_editor"
                """
            )
        )
    importlib.reload(reprexlite.cli)
    assert reprexlite.cli.pyproject_toml_loader.config
    params = reprexlite.cli.app(["--debug"])
    assert params["config"]["editor"] == "test_editor"


@pytest.mark.parametrize("filename", [".reprexlite.toml", "reprexlite.toml"])
def test_reprexlite_toml(project_dir, user_config_dir, filename):
    reprexlite_toml = project_dir / filename
    with reprexlite_toml.open("w") as fp:
        fp.write(
            dedent(
                """\
                editor = "test_editor"
                """
            )
        )
    importlib.reload(reprexlite.cli)
    assert (
        reprexlite.cli.dot_reprexlite_toml_loader.config
        if filename == ".reprexlite.toml"
        else reprexlite.cli.reprexlite_toml_loader.config
    )
    params = reprexlite.cli.app(["--debug"])
    assert params["config"]["editor"] == "test_editor"


def test_user_config_dir(project_dir, user_config_dir):
    with (user_config_dir / "config.toml").open("w") as fp:
        fp.write(
            dedent(
                """\
                editor = "test_editor"
                """
            )
        )
    assert reprexlite.cli.user_reprexlite_toml_loader.config
    params = reprexlite.cli.app(["--debug"])
    assert params["config"]["editor"] == "test_editor"
