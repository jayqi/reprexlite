import builtins
import sys
from textwrap import dedent

import pytest

from reprexlite.config import ReprexConfig
from reprexlite.exceptions import NotAFormatterError, PygmentsNotFoundError
from reprexlite.formatting import register_formatter
from reprexlite.reprexes import Reprex
from tests.expected_formatted import (
    ASSETS_DIR,
    INPUT,
    MOCK_VERSION,
    MockDateTime,
    MockSessionInfo,
    expected_reprexes,
    expected_reprexes_requires_pygments,
)
from tests.utils import assert_str_equals, requires_no_pygments, requires_pygments


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
def test_reprex_formatting(ereprex, patch_datetime, patch_session_info, patch_version):
    """Test that venue formatting works in basic cases."""
    r = Reprex.from_input(INPUT, ReprexConfig(**ereprex.kwargs))
    actual = r.format()
    with (ASSETS_DIR / ereprex.filename).open("r") as fp:
        assert str(actual) == fp.read()
        assert str(actual).endswith("\n")


@requires_pygments
@pytest.mark.parametrize(
    "ereprex",
    expected_reprexes_requires_pygments,
    ids=[e.filename for e in expected_reprexes_requires_pygments],
)
def test_reprex_formatting_requires_pygments(
    ereprex, patch_datetime, patch_session_info, patch_version
):
    """Test that venue formatting works in basic cases."""
    r = Reprex.from_input(INPUT, ReprexConfig(**ereprex.kwargs))
    actual = r.format()
    with (ASSETS_DIR / ereprex.filename).open("r") as fp:
        assert str(actual) == fp.read()
        assert str(actual).endswith("\n")


@requires_no_pygments
def test_html_no_pygments(patch_datetime, patch_version):
    """Test that html produces the same thing as htmlnocolor when pygments is not installed."""
    r_html = Reprex.from_input(INPUT, ReprexConfig(venue="html"))
    actual_html = r_html.format()

    r_htmlnocolor = Reprex.from_input(INPUT, ReprexConfig(venue="htmlnocolor"))
    actual_htmlnocolor = r_htmlnocolor.format()

    assert_str_equals(str(actual_htmlnocolor), str(actual_html))


@requires_no_pygments
def test_rtf_no_pygments(patch_datetime, patch_version):
    with pytest.raises(PygmentsNotFoundError):
        r = Reprex.from_input(INPUT, ReprexConfig(venue="rtf"))
        r.format()


# def test_rtf_pygments_bad_dependency(patch_datetime, patch_version, pygments_bad_dependency):
#     """Test that a bad import inside pygments does not trigger PygmentsNotFoundError"""
#     with pytest.raises(ModuleNotFoundError) as exc_info:
#         r = Reprex.from_input(INPUT, ReprexConfig(venue="rtf"))
#         r.format()
#     assert not isinstance(exc_info.type, PygmentsNotFoundError)
#     assert exc_info.value.name != "pygments"
#     assert exc_info.value.name == pygments_bad_dependency


# def test_not_a_formatter_error():
#     with pytest.raises(NotAFormatterError):

#         @register_formatter("l33t", label="l33t")
#         class F0rm4tt3r:
#             pass
