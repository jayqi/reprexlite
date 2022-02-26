from textwrap import dedent

from reprexlite.reprexes import Reprex


def test_reprex_from_input():
    input = dedent(
        """\
        import math

        def sqrt(x):
            return math.sqrt(x)

        # Here's a comment
        sqrt(4)
        #> 2.0
        """
    ).strip()

    assert Reprex.from_input(input).format() == input
