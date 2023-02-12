import re

# https://stackoverflow.com/a/14693789/5957621
ANSI_ESCAPE_REGEX = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


def remove_ansi_escape(s: str) -> str:
    return ANSI_ESCAPE_REGEX.sub("", s)


def assert_str_equals(expected: str, actual: str):
    to_print = "\n".join(
        [
            "",
            "---EXPECTED---",
            expected,
            "---ACTUAL-----",
            actual,
            "--------------",
        ]
    )
    assert expected == actual, to_print
