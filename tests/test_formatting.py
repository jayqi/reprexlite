import builtins
import sys
from textwrap import dedent

import pytest

from reprexlite.exceptions import NotAFormatterError, PygmentsNotFoundError
from reprexlite.formatting import register_formatter
from reprexlite.reprexes import reprex
from tests.expected_formatted import (
    ASSETS_DIR,
    INPUT,
    MOCK_VERSION,
    MockDateTime,
    MockSessionInfo,
    expected_reprexes,
)


@pytest.fixture
def patch_datetime(monkeypatch):
    monkeypatch.setattr(sys.modules["reprexlite.formatting"], "datetime", MockDateTime)


@pytest.fixture
def patch_version(monkeypatch):
    monkeypatch.setattr(sys.modules["reprexlite.formatting"], "__version__", MOCK_VERSION)


@pytest.fixture
def patch_session_info(monkeypatch):
    monkeypatch.setattr(sys.modules["reprexlite.formatting"], "SessionInfo", MockSessionInfo)


@pytest.mark.parametrize("ereprex", expected_reprexes, ids=[e.filename for e in expected_reprexes])
def test_reprex(ereprex, patch_datetime, patch_session_info, patch_version):
    actual = reprex(INPUT, **ereprex.kwargs, print_=False)
    with (ASSETS_DIR / ereprex.filename).open("r") as fp:
        assert str(actual) + "\n" == fp.read()


@pytest.fixture
def no_pygments(monkeypatch):
    import_orig = builtins.__import__

    def mocked_import(name, *args):
        if name.startswith("pygments"):
            raise ModuleNotFoundError(name="pygments")
        return import_orig(name, *args)

    monkeypatch.setattr(builtins, "__import__", mocked_import)


def test_html_no_pygments(patch_datetime, patch_version, no_pygments):
    actual = reprex(INPUT, venue="html")
    expected = dedent(
        """
        <pre><code>x = 2
        x + 2
        #> 4</code></pre>
        <p><sup>Created at DATETIME by <a href="https://github.com/jayqi/reprexlite">reprexlite</a> vVERSION</sup></p>
        """  # noqa: E501
    ).strip()
    assert str(actual) == expected


def test_rtf_no_pygments(patch_datetime, patch_version, no_pygments):
    with pytest.raises(PygmentsNotFoundError):
        reprex(INPUT, venue="rtf")


@pytest.fixture
def pygments_bad_dependency(monkeypatch):
    """ModuleNotFoundError inside pygments"""
    module_name = "dependency_of_pygments"
    import_orig = builtins.__import__

    def mocked_import(name, *args):
        if name.startswith("pygments"):
            raise ModuleNotFoundError(name=module_name)
        return import_orig(name, *args)

    monkeypatch.setattr(builtins, "__import__", mocked_import)
    yield module_name


def test_rtf_pygments_bad_dependency(patch_datetime, patch_version, pygments_bad_dependency):
    """Test that a bad import inside pygments does not trigger PygmentsNotFoundError"""
    with pytest.raises(ModuleNotFoundError) as exc_info:
        reprex(INPUT, venue="rtf")
    assert not isinstance(exc_info.type, PygmentsNotFoundError)
    assert exc_info.value.name != "pygments"
    assert exc_info.value.name == pygments_bad_dependency


def test_not_a_formatter_error():
    with pytest.raises(NotAFormatterError):

        @register_formatter("l33t")
        class F0rm4tt3r:
            pass
