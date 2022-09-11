import re

# https://stackoverflow.com/a/14693789/5957621
ANSI_ESCAPE_REGEX = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


def remove_ansi_escape(s: str) -> str:
    return ANSI_ESCAPE_REGEX.sub("", s)