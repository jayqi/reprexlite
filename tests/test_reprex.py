import builtins
from textwrap import dedent

import pytest

from reprexlite.code import CodeBlock
from reprexlite.reprex import venues_dispatcher


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
def no_pygments(monkeypatch):
    import_orig = builtins.__import__

    def mocked_import(name, globals, locals, fromlist, level):
        if "pygments" in name:
            raise ImportError()
        return import_orig(name, locals, fromlist, level)

    monkeypatch.setattr(builtins, "__import__", mocked_import)


@pytest.mark.parametrize("venue", set(venues_dispatcher.keys()).difference({"rtf"}))
def test_venue_formatter(venue, no_pygments):
    reprex_class = venues_dispatcher[venue]
    reprex = reprex_class(CodeBlock(INPUT))
    print(reprex)
    assert EXPECTED.strip() in str(reprex)
