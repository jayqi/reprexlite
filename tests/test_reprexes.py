from collections import namedtuple
from textwrap import dedent

import pytest

from reprexlite.config import ReprexConfig
from reprexlite.reprexes import Reprex
from tests.utils import assert_str_equals

Case = namedtuple("Case", ["id", "input", "expected"])

cases = [
    Case(
        id="list comprehension",
        input="""\
        arr = [1, 2, 3, 4, 5]
        [x + 1 for x in arr]
        """,
        expected="""\
        arr = [1, 2, 3, 4, 5]
        [x + 1 for x in arr]
        #> [2, 3, 4, 5, 6]
        """,
    ),
    Case(
        id="if-else",
        input="""\
        status = False

        if status:
            # if True
            x = 1
        else:
            # if False
            x = 0
        x
        """,
        expected="""\
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
    Case(
        id="function def",
        input="""\
        def add_one(x: int):
            return x + 1

        add_one(1)
        """,
        expected="""\
        def add_one(x: int):
            return x + 1

        add_one(1)
        #> 2
        """,
    ),
    Case(
        id="leading/trailing comments",
        input="""\
        # Here's a comment
        x = 1
        x + 1

        # Here's another
        """,
        expected="""\
        # Here's a comment
        x = 1
        x + 1
        #> 2

        # Here's another
        """,
    ),
    Case(
        id="import module",
        input="""\
        import math

        math.factorial(10)
        """,
        expected="""\
        import math

        math.factorial(10)
        #> 3628800
        """,
    ),
    Case(
        id="import module w/ comments",
        input="""\
        import math


        # here's a comment
        math.factorial(10)
        """,
        expected="""\
        import math


        # here's a comment
        math.factorial(10)
        #> 3628800
        """,
    ),
    Case(
        id="stdout",
        input="""\
        arr = [1, 2, 3, 4, 5]
        print(f"start: {arr[0]}, end: {arr[-1]}")
        [x + 1 for x in arr]
        """,
        expected="""\
        arr = [1, 2, 3, 4, 5]
        print(f"start: {arr[0]}, end: {arr[-1]}")
        #> start: 1, end: 5
        [x + 1 for x in arr]
        #> [2, 3, 4, 5, 6]
        """,
    ),
    Case(
        id="return None",
        input="""\
        def return_none():
            return None

        return_none()
        """,
        expected="""\
        def return_none():
            return None

        return_none()
        """,
    ),
    Case(
        id="exception",
        input="""\
        import math

        def sqrt(x):
            return math.sqrt(x)

        sqrt("four")
        """,
        expected="""\
        import math

        def sqrt(x):
            return math.sqrt(x)

        sqrt("four")
        #> Traceback (most recent call last):
        #>   File "<string>", line 1, in <module>
        #>   File "<string>", line 2, in sqrt
        #> TypeError: must be real number, not str
        """,
    ),
    Case(
        id="try-except",
        input="""\
        class MyException(Exception): ...

        try:
            raise MyException
        except MyException:
            print("caught")
        """,
        expected="""\
        class MyException(Exception): ...

        try:
            raise MyException
        except MyException:
            print("caught")
        #> caught
        """,
    ),
    Case(
        id="__name__",
        input="""\
        __name__

        class MyClass: ...
        MyClass.__module__
        """,
        expected="""\
        __name__
        #> '__reprex__'

        class MyClass: ...
        MyClass.__module__
        #> '__reprex__'
        """,
    ),
]


@pytest.mark.parametrize("case", cases, ids=(c.id for c in cases))
def test_reprex_from_input(case):
    """Test that Reprex.from_input parses inputs as expected and evaluates to correct results."""
    r = Reprex.from_input(dedent(case.input))

    assert_str_equals(dedent(case.expected), str(r))


@pytest.mark.parametrize("case", cases, ids=(c.id for c in cases))
def test_reprex_from_input_with_old_results(case):
    """Test that Reprex.from_input parses inputs with old results as expected."""
    r = Reprex.from_input(dedent(case.expected))

    assert r.results_match()
    assert_str_equals(dedent(case.expected), str(r))


def test_keep_old_results():
    """Test that Reprex output with old results is as expected."""
    input = dedent(
        """\
        2+2
        #> 4

        "a" + "b"
        #> 'ab'
        """
    )
    expected = dedent(
        """\
        2+2
        #> #> 4
        #> 4

        "a" + "b"
        #> #> 'ab'
        #> 'ab'
        """
    )
    r = Reprex.from_input(input, config=ReprexConfig(keep_old_results=True))
    assert r.results_match()
    assert_str_equals(expected, str(r))


def test_reprex_auto_parse_doctest():
    """Test that Reprex works with doctest input as expected."""
    input = dedent(
        """\
        >>> 2+2
        4

        >>> for i in range(2):
        ...     print(i)
        0
        1
        """
    )
    expected = dedent(
        """\
        2+2
        #> 4

        for i in range(2):
            print(i)
        #> 0
        #> 1
        """
    )
    r = Reprex.from_input(input)
    assert r.results_match()
    assert_str_equals(expected, str(r))


def test_reprex_custom_input_format():
    """Test that Reprex works with doctest input as expected."""
    input = dedent(
        """\
        aaaa 2+2
        cc 4

        aaaa for i in range(2):
        bbbb     print(i)
        cc 0
        cc 1
        """
    )
    expected = dedent(
        """\
        2+2
        #> 4

        for i in range(2):
            print(i)
        #> 0
        #> 1
        """
    )
    r = Reprex.from_input(
        input,
        config=ReprexConfig(
            parsing_method="declared",
            input_prompt="aaaa",
            input_continuation="bbbb",
            input_comment="cc",
        ),
    )
    assert r.results_match()
    assert_str_equals(expected, str(r))
