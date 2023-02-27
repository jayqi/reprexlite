import builtins
from collections import namedtuple
from textwrap import dedent

import pytest

from reprexlite.config import ReprexConfig
from reprexlite.exceptions import BlackNotFoundError, UnexpectedError
from reprexlite.reprexes import ParsedResult, RawResult, Reprex, reprex
from tests.utils import (
    assert_equals,
    assert_not_equals,
    assert_str_equals,
    requires_no_black,
    requires_no_pygments,
)

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

    assert r.results_match
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
    assert r.results_match
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
    assert r.results_match
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
    assert r.results_match
    assert_str_equals(expected, str(r))


def test_reprex_custom_output_prompts_auto_parsing():
    """Test that Reprex works with custom output prompts."""
    input = dedent(
        """\
        2+2
        #> 4

        # I'm a comment
        for i in range(2):
            print(i)
        #> 0
        #> 1
        """
    )
    expected = dedent(
        """\
        $$$$ 2+2
        || 4
        $$$$
        $$$$ # I'm a comment
        $$$$ for i in range(2):
        ----     print(i)
        || 0
        || 1
        """
    )
    r = Reprex.from_input(
        input,
        config=ReprexConfig(
            prompt="$$$$", continuation="----", comment="||", parsing_method="auto"
        ),
    )
    assert r.results_match
    assert_str_equals(expected, str(r))


def test_reprex_custom_prompts_input_and_output():
    """Test that Reprex works with custom prompts for both input and output."""
    input = dedent(
        """\
        $$$$ 2+2
        || 4
        $$$$
        $$$$ # I'm a comment
        $$$$ for i in range(2):
        ----     print(i)
        || 0
        || 1
        """
    )
    r = Reprex.from_input(
        input,
        config=ReprexConfig(
            prompt="$$$$", continuation="----", comment="||", parsing_method="declared"
        ),
    )
    assert r.results_match
    assert_str_equals(input, str(r))


def test_reprex_custom_prompts_different_input_and_output():
    """Test that Reprex works with different custom prompts for input and output."""
    input = dedent(
        """\
        ! 2+2
        ?? 4
        !
        ! # I'm a comment
        ! for i in range(2):
        *     print(i)
        ?? 0
        ?? 1
        """
    )
    expected = dedent(
        """\
        $$$$ 2+2
        || 4
        $$$$
        $$$$ # I'm a comment
        $$$$ for i in range(2):
        ----     print(i)
        || 0
        || 1
        """
    )
    r = Reprex.from_input(
        input,
        config=ReprexConfig(
            prompt="$$$$",
            continuation="----",
            comment="||",
            input_prompt="!",
            input_continuation="*",
            input_comment="??",
            parsing_method="declared",
        ),
    )
    assert r.results_match
    assert_str_equals(expected, str(r))


def test_reprex_doctest_output():
    input = dedent(
        """\
        2+2
        #> 4

        # I'm a comment
        for i in range(2):
            print(i)
        #> 0
        #> 1
        """
    )
    expected = dedent(
        """\
        >>> 2+2
        4
        >>>
        >>> # I'm a comment
        >>> for i in range(2):
        ...     print(i)
        0
        1
        """
    )
    r = Reprex.from_input(
        input,
        config=ReprexConfig(
            prompt=">>>",
            continuation="...",
            comment="",
        ),
    )
    assert r.results_match
    assert_str_equals(expected, str(r))


def test_trailing_results_no_newline():
    """Test case with trailing results and no newline"""
    input = "2+2\n#> 4"
    r = Reprex.from_input(input, config=ReprexConfig())
    assert r.results_match
    assert_str_equals(input + "\n", str(r))


def test_statement_repr():
    r = Reprex.from_input("2+2")
    assert repr(r.statements[0]) == "<Statement '2+2'>"
    r = Reprex.from_input("12345+67890")
    assert repr(r.statements[0]) == "<Statement '12345+6789...'>"


def test_raw_result_printing():
    config = ReprexConfig()
    # Stdout and raw
    assert str(RawResult(raw=2, stdout="hello", config=config)) == "#> hello\n#> 2"
    # No stdout and raw
    assert str(RawResult(raw=2, stdout=None, config=config)) == "#> 2"
    # Stdout and no raw
    assert str(RawResult(raw=None, stdout="hello", config=config)) == "#> hello"
    # No Stdout and no raw
    with pytest.raises(UnexpectedError):
        str(RawResult(raw=None, stdout=None, config=config))


def test_raw_result_repr():
    config = ReprexConfig()
    assert repr(RawResult(raw=2, stdout=None, config=config)) == "<RawResult '2' 'None'>"
    assert repr(RawResult(raw=None, stdout="hello", config=config)) == "<RawResult 'None' 'hello'>"
    assert repr(RawResult(raw=2, stdout="hello", config=config)) == "<RawResult '2' 'hello'>"
    assert (
        repr(RawResult(raw="12345678901", stdout="abcdefghijk", config=config))
        == "<RawResult '1234567890...' 'abcdefghij...'>"
    )


def test_parsed_result_printing():
    assert str(ParsedResult(lines=["1", "2"], config=ReprexConfig())) == "#> #> 1\n#> #> 2"
    assert (
        str(
            ParsedResult(
                lines=["1", "2"],
                config=ReprexConfig(prompt=">>>", continuation="...", comment=None),
            )
        )
        == "1\n2"
    )

    with pytest.raises(UnexpectedError):
        str(ParsedResult(lines=[], config=ReprexConfig()))


def test_parsed_result_repr():
    config = ReprexConfig()
    assert repr(ParsedResult(lines=["1"], config=config)) == "<ParsedResult '1'>"
    assert repr(ParsedResult(lines=["1", "2"], config=config)) == "<ParsedResult '1\\n2'>"
    assert (
        repr(ParsedResult(lines=[str(i + 1) for i in range(10)], config=config))
        == "<ParsedResult '1\\n2\\n3\\n4...'>"
    )


def test_raw_result_comparisons():
    config = ReprexConfig()

    # equal
    assert_equals(
        RawResult(raw=None, stdout=None, config=config),
        RawResult(raw=None, stdout=None, config=config),
    )
    assert_equals(
        RawResult(raw=1, stdout=None, config=config),
        RawResult(raw=1, stdout=None, config=config),
    )
    assert_equals(
        RawResult(raw=None, stdout="hello", config=config),
        RawResult(raw=None, stdout="hello", config=config),
    )

    # not equal
    assert_not_equals(
        RawResult(raw=None, stdout=None, config=config),
        RawResult(raw=1, stdout=None, config=config),
    )
    assert_not_equals(
        RawResult(raw=None, stdout=None, config=config),
        RawResult(raw=None, stdout="hello", config=config),
    )
    assert_not_equals(
        RawResult(raw=None, stdout=None, config=config),
        RawResult(raw=1, stdout="hello", config=config),
    )
    assert_not_equals(
        RawResult(raw=1, stdout=None, config=config),
        RawResult(raw=2, stdout=None, config=config),
    )
    assert_not_equals(
        RawResult(raw=None, stdout="hello", config=config),
        RawResult(raw=None, stdout="goodbye", config=config),
    )
    assert_not_equals(
        RawResult(raw=1, stdout="hello", config=config),
        RawResult(raw=2, stdout="hello", config=config),
    )
    assert_not_equals(
        RawResult(raw=1, stdout="hello", config=config),
        RawResult(raw=1, stdout="goodbye", config=config),
    )
    assert_not_equals(
        RawResult(raw=1, stdout="hello", config=config),
        RawResult(raw=2, stdout="goodbye", config=config),
    )
    assert_not_equals(
        RawResult(raw=1, stdout=None, config=config),
        1,
    )


def test_parsed_result_comparisions():
    config = ReprexConfig()

    # equal
    assert_equals(
        ParsedResult(lines=[], config=config),
        ParsedResult(lines=[], config=config),
    )
    assert_equals(
        ParsedResult(lines=["hello", "1"], config=config),
        ParsedResult(lines=["hello", "1"], config=config),
    )

    # not equal
    assert_not_equals(
        ParsedResult(lines=[], config=config),
        ParsedResult(lines=["hello"], config=config),
    )
    assert_not_equals(
        ParsedResult(lines=["hello", "1"], config=config),
        ParsedResult(lines=["goodbye", "1"], config=config),
    )
    assert_not_equals(
        ParsedResult(lines=["hello"], config=config),
        "hello",
    )


def test_raw_result_to_parsed_result_comparisons():
    config = ReprexConfig()

    # equal
    assert_equals(
        RawResult(raw=None, stdout=None, config=config),
        ParsedResult(lines=[], config=config),
    )
    assert_equals(
        RawResult(raw=2, stdout=None, config=config),
        ParsedResult(lines=["2"], config=config),
    )
    assert_equals(
        RawResult(raw=None, stdout="hello", config=config),
        ParsedResult(lines=["hello"], config=config),
    )
    assert_equals(
        RawResult(raw=2, stdout="hello", config=config),
        ParsedResult(lines=["hello", "2"], config=config),
    )

    # not equal
    assert_not_equals(
        RawResult(raw=None, stdout=None, config=config),
        ParsedResult(lines=["1"], config=config),
    )
    assert_not_equals(
        RawResult(raw=1, stdout=None, config=config),
        ParsedResult(lines=[], config=config),
    )
    assert_not_equals(
        RawResult(raw=None, stdout="hello", config=config),
        ParsedResult(lines=[], config=config),
    )
    assert_not_equals(
        RawResult(raw=1, stdout=None, config=config),
        ParsedResult(lines=["2"], config=config),
    )
    assert_not_equals(
        RawResult(raw=None, stdout="hello", config=config),
        ParsedResult(lines=["goodbye"], config=config),
    )
    assert_not_equals(
        RawResult(raw=1, stdout="hello", config=config),
        ParsedResult(lines=["goodbye", "2"], config=config),
    )
    assert_not_equals(
        RawResult(raw=1, stdout=None, config=config),
        ParsedResult(lines=["hello", "1"], config=config),
    )
    assert_not_equals(
        RawResult(raw=None, stdout="hello", config=config),
        ParsedResult(lines=["hello", "1"], config=config),
    )


@requires_black
def test_style_with_black():
    input = dedent(
        """\
        [1, 2,]
        """
    )
    expected = dedent(
        """\
        [
            1,
            2,
        ]
        """
    )
    reprex = Reprex.from_input(input=input, config=ReprexConfig(style=True))
    reprex.statements[0].raw_code == input.strip()
    reprex.statements[0].raw_code == expected.strip()


@requires_no_black
def test_no_black(no_black):
    with pytest.raises(BlackNotFoundError):
        reprex = Reprex.from_input("2+2", config=ReprexConfig(style=True))
        reprex.format()


@pytest.fixture
def black_bad_dependency(monkeypatch):
    """ModuleNotFoundError inside black"""
    module_name = "dependency_of_black"
    import_orig = builtins.__import__

    def mocked_import(name, *args):
        if name.startswith("black"):
            raise ModuleNotFoundError(name=module_name)
        return import_orig(name, *args)

    monkeypatch.setattr(builtins, "__import__", mocked_import)
    yield module_name


def test_black_bad_dependency(black_bad_dependency, monkeypatch):
    with pytest.raises(ModuleNotFoundError) as exc_info:
        reprex = Reprex.from_input("2+2", config=ReprexConfig(style=True))
        reprex.format()
    assert not isinstance(exc_info.type, BlackNotFoundError)
    assert exc_info.value.name != "black"
    assert exc_info.value.name == black_bad_dependency


@requires_no_pygments
def test_no_pygments_terminal():
    """Test that format for terminal works even if pygments is not installed."""
    r = Reprex.from_input("2+2")
    assert_str_equals(r.format(terminal=False), r.format(terminal=True))


def test_repr_html():
    """Test rich HTML display for Jupyter Notebooks runs without error."""
    r = Reprex.from_input("2+2")
    r._repr_html_()


@requires_no_pygments
def test_repr_html_no_pygments(no_pygments):
    """Test that rich HTML display for Jupyter Notebooks runs without error even if pygments is not
    installed."""
    r = Reprex.from_input("2+2")
    r._repr_html_()


def test_reprex_init_bad_lengths_error():
    r = Reprex.from_input("2+2")
    with pytest.raises(UnexpectedError):
        Reprex(
            config=ReprexConfig(),
            statements=r.statements,
            results=r.results,
            old_results=[],
            scope=r.scope,
        )


def test_reprex_function(tmp_path):
    input = "2+2"
    expected = Reprex.from_input(input)
    actual = reprex("2+2", outfile=tmp_path / "rendered.txt")

    assert actual == expected

    # Test writing to file
    with (tmp_path / "rendered.txt").open("r") as fp:
        assert expected.format() == fp.read()
