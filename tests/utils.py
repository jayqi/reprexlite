from contextlib import contextmanager
import re
import sys
from typing import Any

from reprexlite.session_info import Package, SessionInfo

# https://stackoverflow.com/a/14693789/5957621
ANSI_ESCAPE_REGEX = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


def remove_ansi_escape(s: str) -> str:
    return ANSI_ESCAPE_REGEX.sub("", s)


def assert_str_equals(expected: str, actual: str):
    """Tests that strings are equivalent and prints out both if failure."""
    to_print = "\n".join(
        [
            "",
            "---EXPECTED---",
            expected,
            "---ACTUAL-----",
            actual,
            "--------------",
        ]
    )
    assert expected == actual, to_print


def assert_equals(left: Any, right: Any):
    """Tests equals in both directions"""
    assert left == right
    assert right == left


def assert_not_equals(left: Any, right: Any):
    """Tests not equals in both directions"""
    assert left != right
    assert right != left


MOCK_VERSION = "VERSION"


@contextmanager
def patch_version():
    version = sys.modules["reprexlite.rendering"].__version__
    sys.modules["reprexlite.rendering"].__version__ = MOCK_VERSION
    yield
    sys.modules["reprexlite.rendering"].__version__ = version


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
    datetime = sys.modules["reprexlite.rendering"].datetime
    sys.modules["reprexlite.rendering"].datetime = MockDateTime
    yield
    sys.modules["reprexlite.rendering"].datetime = datetime


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
    sys.modules["reprexlite.rendering"].SessionInfo = MockSessionInfo
    yield
    sys.modules["reprexlite.rendering"].SessionInfo = SessionInfo
