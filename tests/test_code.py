from collections import namedtuple
from textwrap import dedent

import pytest

from reprexlite.code import CodeBlock
from tests.utils import assert_doctest, cprint

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
        #> None
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
]


@pytest.mark.parametrize("case", cases, ids=(c.id for c in cases))
def test_code_block(case):
    code_block = CodeBlock.parse_and_evaluate(dedent(case.input))
    cprint("---")
    cprint(str(code_block))
    cprint("---")
    cprint(dedent(case.expected))
    cprint("---")
    assert str(code_block) == dedent(case.expected).strip()


def test_format_doctest():
    input = dedent(
        """\
        # Top comment
        status = False

        if status:
            # if True
            x = 1
        else:
            # if False
            x = 0
        x
        import math


        # here's a comment
        math.factorial(10)
        """
    )
    actual = CodeBlock.parse_and_evaluate(input).format(
        prompt=">>>", continuation="...", comment=""
    )
    expected = dedent(
        """\
        >>> # Top comment
        >>> status = False
        >>> \n        >>> if status:
        ...     # if True
        ...     x = 1
        ... else:
        ...     # if False
        ...     x = 0
        >>> x
        0
        >>> import math
        >>> \n        >>> \n        >>> # here's a comment
        >>> math.factorial(10)
        3628800
        """
    )
    cprint("---input---")
    cprint(input)
    cprint("---actual---")
    cprint(actual)
    cprint("---expected---")
    cprint(expected)
    assert actual == expected
    assert_doctest(actual)
