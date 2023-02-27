import re
from typing import Any

import pytest

## SKIP DECORATORS

requires_ipython = pytest.mark.skipif(
    not pytest.IPYTHON_IS_AVAILABLE, reason="ipython is not available"
)
requires_no_ipython = pytest.mark.skipif(
    pytest.IPYTHON_IS_AVAILABLE, reason="ipython is available"
)
requires_black = pytest.mark.skipif(not pytest.BLACK_IS_AVAILABLE, reason="black is not available")
requires_no_black = pytest.mark.skipif(pytest.BLACK_IS_AVAILABLE, reason="black is available")
requires_pygments = pytest.mark.skipif(
    not pytest.PYGMENTS_IS_AVAILABLE, reason="pygments is not available"
)
requires_no_pygments = pytest.mark.skipif(
    pytest.PYGMENTS_IS_AVAILABLE, reason="pygments is available"
)


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
