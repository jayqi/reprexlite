from contextlib import redirect_stdout
import io
from itertools import chain
import sys

import pytest

from reprexlite.config import ReprexConfig
import reprexlite.printing
from reprexlite.reprexes import Reprex
from tests.expected_printed import ASSETS_DIR, INPUT, expected_reprexes, expected_reprexes_no_color
from tests.pytest_utils import requires_no_rich, requires_rich
from tests.utils import (
    MOCK_VERSION,
    MockDateTime,
    assert_str_equals,
)

all_expected_reprexes = list(chain(expected_reprexes, expected_reprexes_no_color))


@pytest.fixture
def patch_datetime(monkeypatch):
    monkeypatch.setattr(sys.modules["reprexlite.formatting"], "datetime", MockDateTime)


@pytest.fixture
def patch_version(monkeypatch):
    monkeypatch.setattr(sys.modules["reprexlite.formatting"], "__version__", MOCK_VERSION)


@pytest.fixture
def patch_rich_force_terminal(monkeypatch):
    from rich.console import Console

    force_terminal_console = Console(soft_wrap=True, force_terminal=True)
    monkeypatch.setattr(reprexlite.printing, "console", force_terminal_console)


@requires_rich
@pytest.mark.parametrize(
    "ereprex", all_expected_reprexes, ids=[e.filename for e in all_expected_reprexes]
)
def test_reprex_printing(ereprex, patch_datetime, patch_version, patch_rich_force_terminal):
    """Test that printing works."""
    r = Reprex.from_input(INPUT, ReprexConfig(**ereprex.kwargs))

    with io.StringIO() as buffer:
        with redirect_stdout(buffer):
            r.print()
        buffer.seek(0)
        actual = buffer.read()

    with (ASSETS_DIR / ereprex.filename).open("r") as fp:
        assert_str_equals(expected=fp.read(), actual=actual)
        assert str(actual).endswith("\n")


@requires_no_rich
@pytest.mark.parametrize(
    "ereprex", expected_reprexes_no_color, ids=[e.filename for e in expected_reprexes_no_color]
)
def test_reprex_printing_no_rich(ereprex, patch_datetime, patch_version):
    """Test that printing works when rich is not available and produces the same output as
    no_color=True."""
    kwargs = ereprex.kwargs.copy()
    kwargs.pop("no_color")

    ## default
    r = Reprex.from_input(INPUT, ReprexConfig(**kwargs))

    with io.StringIO() as buffer:
        with redirect_stdout(buffer):
            r.print()
        buffer.seek(0)
        actual = buffer.read()

    with (ASSETS_DIR / ereprex.filename).open("r") as fp:
        assert_str_equals(expected=fp.read(), actual=actual)
        assert str(actual).endswith("\n")

    # no_color=True
    r = Reprex.from_input(INPUT, ReprexConfig(**kwargs, no_color=True))

    with io.StringIO() as buffer:
        with redirect_stdout(buffer):
            r.print()
        buffer.seek(0)
        actual = buffer.read()

    with (ASSETS_DIR / ereprex.filename).open("r") as fp:
        assert_str_equals(expected=fp.read(), actual=actual)
        assert str(actual).endswith("\n")
