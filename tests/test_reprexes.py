from collections import namedtuple
from textwrap import dedent

import pytest

from reprexlite.reprexes import Reprex

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
    r = Reprex.from_input(dedent(case.input)).to_evaluated()
    rr = r.to_evaluated()  # Evaluation should be idempotent with default configuration

    print("\n---EXPECTED---\n")
    print(dedent(case.expected))
    print("\n---ACTUAL 1-----\n")
    print(str(r))
    print("\n---ACTUAL 2-----\n")
    print(str(r))
    print("\n--------------\n")

    assert str(r) == dedent(case.expected.rstrip())
    assert str(rr) == dedent(case.expected.rstrip())


def test_keep_old_results():
    pass
