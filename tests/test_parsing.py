from collections import namedtuple
from textwrap import dedent

import pytest

from reprexlite.exceptions import InvalidInputPrefixes
from reprexlite.parsing import _parse, parse_input_to_code

Case = namedtuple("Case", ["id", "input"])

cases = [
    Case(
        id="default reprex",
        input="""\
        def add_one(x: int):
            return x + 1

        # Now add 1
        add_one(1)
        #> 2
        """,
    ),
    Case(
        id="doctest",
        input="""\
        >>> def add_one(x: int):
        ...     return x + 1
        ...
        >>> # Now add 1
        >>> add_one(1)
        2
        """,
    ),
]


expected_by_keep_old_results = {
    True: """\
    def add_one(x: int):
        return x + 1

    # Now add 1
    add_one(1)
    # 2
    """,
    False: """\
    def add_one(x: int):
        return x + 1

    # Now add 1
    add_one(1)
    """,
}


@pytest.mark.parametrize("case", cases, ids=(c.id for c in cases))
@pytest.mark.parametrize("keep_old_results", [True, False])
def test_parse(case, keep_old_results):
    input = dedent(case.input)
    parsed = parse_input_to_code(input, keep_old_results=keep_old_results)
    expected = dedent(expected_by_keep_old_results[keep_old_results])
    print("---input---")
    print(input)
    print("---parsed---")
    print(parsed)
    print("---expected---")
    print(expected)

    assert parsed == expected


@pytest.mark.parametrize("keep_old_results", [True, False])
def test_parse_custom_comment(keep_old_results):
    input = dedent(
        """\
        def add_one(x: int):
            return x + 1

        # Now add 1
        add_one(1)
        ## 2
        """
    )

    parsed = parse_input_to_code(input, comment="##", keep_old_results=keep_old_results)
    expected = dedent(expected_by_keep_old_results[keep_old_results])

    print("---input---")
    print(input)
    print("---parsed---")
    print(parsed)
    print("---expected---")
    print(expected)

    assert parsed == expected


@pytest.mark.parametrize("keep_old_results", [True, False])
def test_parse_custom_prompt(keep_old_results):
    input = dedent(
        """\
        $ def add_one(x: int):
              return x + 1
          \n        $ # Now add 1
        $ add_one(1)
        2
        """
    )

    parsed = parse_input_to_code(
        input, prompt="$", continuation=" ", keep_old_results=keep_old_results
    )
    expected = dedent(expected_by_keep_old_results[keep_old_results])

    print("---input---")
    print(input)
    print("---parsed---")
    print(parsed)
    print("---expected---")
    print(expected)

    assert parsed == expected


@pytest.mark.parametrize("keep_old_results", [True, False])
def test_parse_custom_all(keep_old_results):
    input = dedent(
        """\
        $ def add_one(x: int):
              return x + 1
          \n        $ # Now add 1
        $ add_one(1)
        ## 2
        """
    )

    parsed = parse_input_to_code(
        input, prompt="$", continuation=" ", comment="##", keep_old_results=keep_old_results
    )
    expected = dedent(expected_by_keep_old_results[keep_old_results])

    print("---input---")
    print(input)
    print("---parsed---")
    print(parsed)
    print("---expected---")
    print(expected)

    assert parsed == expected


def test_all_none_invalid():
    with pytest.raises(InvalidInputPrefixes):
        _parse(cases[0].input)

    with pytest.raises(InvalidInputPrefixes):
        _parse(cases[0].input, prompt="", continuation="", comment="")
