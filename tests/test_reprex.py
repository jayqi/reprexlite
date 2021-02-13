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
    ),
    TestCase(
        """\
        status = False
        if status:
            # if True
            x = 1
        else:
            # if False
            x = 0
        x
        """,
        """\
        status = False
        if status:
            # if True
            x = 1
        else:
            # if False
            x = 0
        x
        #> 0
        """,
    ),
    TestCase(
        """\
        def add_one(x: int):
            return x + 1
        add_one(1)
        """,
        """\
        def add_one(x: int):
            return x + 1
        add_one(1)
        #> 2
        """,
    ),
    TestCase(
        """\
        # Here's a comment
        x = 1
        x + 1
        # Here's another
        """,
        """\
        # Here's a comment
        x = 1
        x + 1
        #> 2
        # Here's another
        """,
    ),
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
