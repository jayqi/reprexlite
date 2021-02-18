from collections import namedtuple
from pathlib import Path
from textwrap import dedent

import pytest

from reprexlite.code import CodeBlock

REPO_ROOT = Path(__file__).parents[1].resolve()

Case = namedtuple("Case", ["input", "expected"])

cases = [
    Case(
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
    Case(
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
    Case(
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
    Case(
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
    Case(
        """\
        import math

        math.factorial(10)
        """,
        """\
        import math

        math.factorial(10)
        #> 3628800
        """,
    ),
    Case(
        """\
        import math


        # here's a comment
        math.factorial(10)
        """,
        """\
        import math


        # here's a comment
        math.factorial(10)
        #> 3628800
        """,
    ),
    Case(
        """\
        arr = [1, 2, 3, 4, 5]
        print(f"start: {arr[0]}, end: {arr[-1]}")
        [x + 1 for x in arr]
        """,
        """\
        arr = [1, 2, 3, 4, 5]
        print(f"start: {arr[0]}, end: {arr[-1]}")
        #> start: 1, end: 5
        [x + 1 for x in arr]
        #> [2, 3, 4, 5, 6]
        """,
    ),
    Case(
        """\
        def return_none():
            return None

        return_none()
        """,
        """\
        def return_none():
            return None

        return_none()
        #> None
        """,
    ),
    Case(
        """\
        import math

        def sqrt(x):
            return math.sqrt(x)

        sqrt("four")
        """,
        f"""\
        import math

        def sqrt(x):
            return math.sqrt(x)

        sqrt("four")
        #> Traceback (most recent call last):
        #>   File "{REPO_ROOT / "reprexlite" / "code.py"}", line 69, in evaluate
        #>     result = eval(str(self).strip(), scope, scope)
        #>   File "<string>", line 1, in <module>
        #>   File "<string>", line 2, in sqrt
        #> TypeError: must be real number, not str
        """,
    ),
]


@pytest.mark.parametrize("case", cases)
def test_source(case):
    code_block = CodeBlock(dedent(case.input))
    print("---")
    print(str(code_block))
    print("---")
    print(dedent(case.expected))
    print("---")
    assert str(code_block) == dedent(case.expected).strip()


def test_old_results():
    input = dedent(
        """\
        arr = [1, 2, 3, 4, 5]
        [x + 1 for x in arr]
        #> old line
        """
    )

    # old_results = False (default)
    expected_false = dedent(
        """\
        arr = [1, 2, 3, 4, 5]
        [x + 1 for x in arr]
        #> [2, 3, 4, 5, 6]
        """
    )
    assert str(CodeBlock(input)) == expected_false.strip()

    # old_results = True
    expected_true = dedent(
        """\
        arr = [1, 2, 3, 4, 5]
        [x + 1 for x in arr]
        #> [2, 3, 4, 5, 6]
        #> old line
        """
    )
    assert str(CodeBlock(input, old_results=True)) == expected_true.strip()
