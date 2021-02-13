from collections import namedtuple
from textwrap import dedent
from reprexlite.reprex import Reprex

import pytest


TestCase = namedtuple("TestCase", ["input", "expected"])

test_cases = [
    TestCase(
        """\
        arr = [1, 2, 3, 4, 5]
        [x + 1 for x in arr]
        """,
        """\
        arr = [1, 2, 3, 4, 5]
        [x + 1 for x in arr]
        #> [2, 3, 4, 5, 6]
        """,
    )
]


@pytest.mark.parametrize("test_case", test_cases)
def test_source(test_case):
    reprex = Reprex(dedent(test_case.input))
    print("---")
    print(str(reprex))
    print("---")
    print(dedent(test_case.expected))
    print("---")
    assert str(reprex) == dedent(test_case.expected).strip()
