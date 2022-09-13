from textwrap import dedent

import pytest

from reprexlite.exceptions import InvalidInputPrefixesError
from reprexlite.parsing import LineType, auto_parse, parse, parse_doctest, parse_reprex


def test_parse_reprex():
    input = """\
    import math

    def sqrt(x):
        return math.sqrt(x)

    # Here's a comment
    sqrt(4)
    #> 2.0
    """

    actual = list(parse_reprex(dedent(input)))
    expected = [
        ("import math", LineType.CODE),
        ("", LineType.CODE),
        ("def sqrt(x):", LineType.CODE),
        ("    return math.sqrt(x)", LineType.CODE),
        ("", LineType.CODE),
        ("# Here's a comment", LineType.CODE),
        ("sqrt(4)", LineType.CODE),
        ("2.0", LineType.RESULT),
        ("", LineType.CODE),
    ]

    assert actual == expected


def test_parse_doctest():
    input = """\
    >>> import math
    >>>
    >>> def sqrt(x):
    ...     return math.sqrt(x)
    ...
    >>> # Here's a comment
    >>> sqrt(4)
    2.0
    """

    actual = list(parse_doctest(dedent(input)))
    expected = [
        ("import math", LineType.CODE),
        ("", LineType.CODE),
        ("def sqrt(x):", LineType.CODE),
        ("    return math.sqrt(x)", LineType.CODE),
        ("", LineType.CODE),
        ("# Here's a comment", LineType.CODE),
        ("sqrt(4)", LineType.CODE),
        ("2.0", LineType.RESULT),
        ("", LineType.CODE),
    ]

    assert actual == expected


def test_parse_with_both_prompt_and_comment():
    input = """\
    >>> import math
    >>>
    >>> def sqrt(x):
    ...     return math.sqrt(x)
    ...
    >>> # Here's a comment
    >>> sqrt(4)
    #> 2.0
    """

    actual = list(parse(dedent(input), prompt=">>>", continuation="...", comment="#>"))
    expected = [
        ("import math", LineType.CODE),
        ("", LineType.CODE),
        ("def sqrt(x):", LineType.CODE),
        ("    return math.sqrt(x)", LineType.CODE),
        ("", LineType.CODE),
        ("# Here's a comment", LineType.CODE),
        ("sqrt(4)", LineType.CODE),
        ("2.0", LineType.RESULT),
        ("", LineType.CODE),
    ]

    assert actual == expected


def test_parse_all_blank_prefixes():
    input = """\
    2+2
    """
    with pytest.raises(InvalidInputPrefixesError):
        list(parse(dedent(input), prompt=None, continuation=None, comment=None))


def test_auto_parse():
    input_reprex = """\
    import math

    def sqrt(x):
        return math.sqrt(x)

    # Here's a comment
    sqrt(4)
    #> 2.0
    """

    input_doctest = """\
    >>> import math
    >>>
    >>> def sqrt(x):
    ...     return math.sqrt(x)
    ...
    >>> # Here's a comment
    >>> sqrt(4)
    2.0
    """

    expected = [
        ("import math", LineType.CODE),
        ("", LineType.CODE),
        ("def sqrt(x):", LineType.CODE),
        ("    return math.sqrt(x)", LineType.CODE),
        ("", LineType.CODE),
        ("# Here's a comment", LineType.CODE),
        ("sqrt(4)", LineType.CODE),
        ("2.0", LineType.RESULT),
        ("", LineType.CODE),
    ]

    actual_reprex = list(auto_parse(dedent(input_reprex)))
    assert actual_reprex == expected

    actual_doctest = list(auto_parse(dedent(input_doctest)))
    assert actual_doctest == expected
