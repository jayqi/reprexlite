from textwrap import dedent

from reprexlite.parsing import LineType, auto_parse, parse_doctest, parse_reprex


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


def test_auto_parse():
    input = """\
    import math

    def sqrt(x):
        return math.sqrt(x)

    # Here's a comment
    sqrt(4)
    #> 2.0
    """

    actual = list(auto_parse(dedent(input)))
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
