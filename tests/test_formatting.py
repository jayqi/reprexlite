import builtins
import sys
from textwrap import dedent

import pytest

from reprexlite.config import ReprexConfig, Venue
from reprexlite.exceptions import PygmentsNotFoundError
from reprexlite.formatting import formatter_registry
from reprexlite.reprexes import Reprex
from tests.expected_formatted import (
    ASSETS_DIR,
    INPUT,
    MOCK_VERSION,
    MockDateTime,
    MockSessionInfo,
    expected_reprexes,
)
from tests.utils import assert_str_equals


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
    r = Reprex.from_input(INPUT, ReprexConfig(**ereprex.kwargs))
    actual = r.render_and_format()
    with (ASSETS_DIR / ereprex.filename).open("r") as fp:
        assert str(actual) == fp.read()
        assert str(actual).endswith("\n")


@pytest.fixture
def no_pygments(monkeypatch):
    import_orig = builtins.__import__

    def mocked_import(name, *args):
        if name.startswith("pygments"):
            raise ModuleNotFoundError(name="pygments")
        return import_orig(name, *args)

    monkeypatch.setattr(builtins, "__import__", mocked_import)


def test_all_venues_have_formatters():
    for venue in Venue:
        print(venue)
        assert venue in formatter_registry


def test_html_no_pygments(patch_datetime, patch_version, no_pygments):
    r = Reprex.from_input(INPUT, ReprexConfig(venue="html"))
    actual = r.render_and_format()
    expected = dedent(
        """\
        <pre><code>x = 2
        x + 2
        #> 4</code></pre>
        <p><sup>Created at DATETIME by <a href="https://github.com/jayqi/reprexlite">reprexlite</a> vVERSION</sup></p>
        """  # noqa: E501
    )
    assert_str_equals(expected, str(actual))
    assert str(actual).endswith("\n")


def test_rtf_no_pygments(patch_datetime, patch_version, no_pygments):
    with pytest.raises(PygmentsNotFoundError):
        r = Reprex.from_input(INPUT, ReprexConfig(venue="rtf"))
        r.render_and_format()


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
        r = Reprex.from_input(INPUT, ReprexConfig(venue="rtf"))
        r.render_and_format()
    assert not isinstance(exc_info.type, PygmentsNotFoundError)
    assert exc_info.value.name != "pygments"
    assert exc_info.value.name == pygments_bad_dependency
