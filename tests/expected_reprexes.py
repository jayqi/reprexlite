from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
import shutil
import sys
from textwrap import dedent
from typing import Any, Dict

from reprexlite import reprex
from reprexlite.session_info import Package, SessionInfo

ASSETS_DIR = (Path(__file__).parent / "assets").resolve()


INPUT = dedent(
    """\
    x = 2
    x + 2
    """
)


@dataclass
class ExpectedReprex:
    filename: str
    kwargs: Dict[str, Any]


expected_reprexes = [
    # Defaults
    ExpectedReprex("gh.md", {"venue": "gh"}),
    ExpectedReprex("so.md", {"venue": "so"}),
    ExpectedReprex("ds.md", {"venue": "ds"}),
    ExpectedReprex("html.html", {"venue": "html"}),
    ExpectedReprex("py.py", {"venue": "py"}),
    ExpectedReprex("rtf.rtf", {"venue": "rtf"}),
    ExpectedReprex("slack.txt", {"venue": "slack"}),
    # With ad
    ExpectedReprex("ad/gh.md", {"venue": "gh", "advertise": True}),
    ExpectedReprex("ad/so.md", {"venue": "so", "advertise": True}),
    ExpectedReprex("ad/ds.md", {"venue": "ds", "advertise": True}),
    ExpectedReprex("ad/html.html", {"venue": "html", "advertise": True}),
    ExpectedReprex("ad/py.py", {"venue": "py", "advertise": True}),
    ExpectedReprex("ad/rtf.rtf", {"venue": "rtf", "advertise": True}),
    ExpectedReprex("ad/slack.txt", {"venue": "slack", "advertise": True}),
    # No ad
    ExpectedReprex("no_ad/gh.md", {"venue": "gh", "advertise": False}),
    ExpectedReprex("no_ad/so.md", {"venue": "so", "advertise": False}),
    ExpectedReprex("no_ad/ds.md", {"venue": "ds", "advertise": False}),
    ExpectedReprex("no_ad/html.html", {"venue": "html", "advertise": False}),
    ExpectedReprex("no_ad/py.py", {"venue": "py", "advertise": False}),
    ExpectedReprex("no_ad/rtf.rtf", {"venue": "rtf", "advertise": False}),
    ExpectedReprex("no_ad/slack.txt", {"venue": "slack", "advertise": False}),
    # With session info
    ExpectedReprex("session_info/gh.md", {"venue": "gh", "session_info": True}),
    ExpectedReprex("session_info/so.md", {"venue": "so", "session_info": True}),
    ExpectedReprex("session_info/ds.md", {"venue": "ds", "session_info": True}),
    ExpectedReprex("session_info/html.html", {"venue": "html", "session_info": True}),
    ExpectedReprex("session_info/py.py", {"venue": "py", "session_info": True}),
    ExpectedReprex("session_info/rtf.rtf", {"venue": "rtf", "session_info": True}),
    ExpectedReprex("session_info/slack.txt", {"venue": "slack", "session_info": True}),
]

MOCK_VERSION = "VERSION"


@contextmanager
def patch_version():
    version = sys.modules["reprexlite.reprex"].__version__
    sys.modules["reprexlite.reprex"].__version__ = MOCK_VERSION
    yield
    sys.modules["reprexlite.reprex"].__version__ = version


class MockDateTime:
    @classmethod
    def now(cls):
        return cls()

    def astimezone(self):
        return self

    def strftime(self, format):
        return "DATETIME"


@contextmanager
def patch_datetime():

    datetime = sys.modules["reprexlite.reprex"].datetime
    sys.modules["reprexlite.reprex"].datetime = MockDateTime
    yield
    sys.modules["reprexlite.reprex"].datetime = datetime


class MockPackage(Package):
    def __init__(self, name: str, version: str):
        self._name = name
        self._version = version

    @property
    def name(self):
        return self._name

    @property
    def version(self):
        return self._version


class MockSessionInfo(SessionInfo):
    def __init__(self, *args, **kwargs):
        self.python_version = "3.x.y"
        self.python_build_date = "Jan 01 2020 03:33:33"
        self.os = "GLaDOS"
        self.packages = [
            MockPackage("datatable", "1.0"),
            MockPackage("ggplot2", "2.0"),
            MockPackage("pkgnet", "3.0"),
        ]


@contextmanager
def patch_session_info():
    sys.modules["reprexlite.reprex"].SessionInfo = MockSessionInfo
    yield
    sys.modules["reprexlite.reprex"].SessionInfo = SessionInfo


if __name__ == "__main__":
    shutil.rmtree(ASSETS_DIR, ignore_errors=True)
    with patch_datetime(), patch_version(), patch_session_info():
        for ereprex in expected_reprexes:
            outfile = ASSETS_DIR / ereprex.filename
            outfile.parent.mkdir(exist_ok=True)
            reprex(INPUT, outfile=outfile, **ereprex.kwargs)
