import builtins
import sys
from textwrap import dedent

import pytest

from reprexlite.formatting import venues_dispatcher
from reprexlite.reprexes import reprex
from tests.expected_reprexes import (
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


@pytest.fixture
def no_pygments(monkeypatch):
    import_orig = builtins.__import__

    def mocked_import(name, *args):
        if name.startswith("pygments"):
            raise ImportError()
        return import_orig(name, *args)

    monkeypatch.setattr(builtins, "__import__", mocked_import)


@pytest.mark.parametrize("ereprex", expected_reprexes, ids=[e.filename for e in expected_reprexes])
def test_reprex(ereprex, patch_datetime, patch_session_info, patch_version):
    actual = reprex(INPUT, **ereprex.kwargs, print_=False)
    with (ASSETS_DIR / ereprex.filename).open("r") as fp:
        assert str(actual) + "\n" == fp.read()


# def test_html(patch_datetime, patch_version, no_pygments):
#     reprex_class = venues_dispatcher["html"]
#     code_block = CodeBlock(INPUT)
#     reprex = reprex_class(code_block)
#     print(reprex)
#     expected = dedent(
#         """
#         <pre><code>x = 2
#         x + 2
#         #> 4</code></pre>
#         <p><sup>Created at DATETIME by <a href="https://github.com/jayqi/reprexlite">reprexlite</a> vVERSION</sup></p>
#         """
#     ).strip()
#     assert str(reprex) == expected
