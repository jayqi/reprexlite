from datetime import datetime
from enum import Enum
from typing import Callable, Dict

from reprexlite.session_info import SessionInfo
from reprexlite.version import __version__


class Advertisement:
    pkg = "reprexlite"
    url = "https://github.com/jayqi/reprexlite"
    ver = f"v{__version__}"

    def __init__(self):
        now = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
        self.created = f"Created at {now} by"

    def markdown(self) -> str:
        return f"<sup>{self.created} [{self.pkg}]({self.url}) {self.ver}</sup>"

    def html(self) -> str:
        return f'<p><sup>{self.created} <a href="{self.url}">{self.pkg}</a> {self.ver}</p>'

    def code_comment(self) -> str:
        return f"# {self.created} {self.pkg} {self.ver} <{self.url}>"

    def text(self) -> str:
        return f"{self.created} {self.pkg} {self.ver} <{self.url}>"


def markdown(reprex: str, advertise: bool = True, session_info: bool = False) -> str:
    out = "\n".join(
        [
            "```python",
            str(reprex),
            "```",
        ]
    )
    if advertise:
        out += "\n\n" + Advertisement().markdown()
    if session_info:
        out += "\n".join(
            [
                "\n\n<details><summary>Session Info</summary>",
                "```text",
                str(SessionInfo()),
                "```",
                "</details>",
            ]
        )

    return out


def html(reprex: str, advertise: bool = True, session_info: bool = False) -> str:
    try:
        from pygments import highlight
        from pygments.lexers import PythonLexer
        from pygments.formatters import HtmlFormatter

        formatter = HtmlFormatter()
        style = f"<style>{formatter.get_style_defs('.highlight')}</style>"
        code = highlight(str(reprex), PythonLexer(), formatter)
    except ImportError:
        style = ""
        code = f"<pre><code>{reprex}</code></pre>"

    ad = "\n" + Advertisement().html() if advertise else ""
    sess = (
        (
            "\n<details><summary>Session Info</summary>"
            f"<pre><code>{SessionInfo()}</code></pre>"
            "</details>"
        )
        if session_info
        else ""
    )
    return style + code + ad + sess


def py(reprex: str, advertise: bool = False, session_info: bool = False) -> str:
    ad = "\n\n" + Advertisement().code_comment() if advertise else ""
    if session_info:
        sess_lines = str(SessionInfo()).split("\n")
        sess_lines = ["# " + line for line in sess_lines]
        sess = "\n\n" + "\n".join(sess_lines)
    else:
        sess = ""
    return str(reprex) + ad + sess


def rtf(reprex: str, advertise: bool = False, session_info: bool = False) -> str:
    try:
        from pygments import highlight
        from pygments.lexers import PythonLexer
        from pygments.formatters import RtfFormatter
    except ImportError:
        raise ImportError("Pygments is required for RTF output.")
    out = str(reprex)
    if advertise:
        out += "\n\n" + Advertisement().text()
    if session_info:
        out += "\n\n" + SessionInfo()
    return highlight(out, PythonLexer(), RtfFormatter())


def slack(reprex: str, advertise: bool = False, session_info: bool = False) -> str:
    ad = "\n" + Advertisement().text() if advertise else ""
    sess = (
        "\n".join(
            [
                "\n```",
                str(SessionInfo()),
                "```",
            ]
        )
        if session_info
        else ""
    )
    return "\n".join(["```", str(reprex), "```"]) + ad + sess


def display_terminal(reprex: str):
    try:
        from pygments import highlight
        from pygments.lexers import PythonLexer
        from pygments.formatters import Terminal256Formatter

        return highlight(str(reprex), PythonLexer(), Terminal256Formatter()).strip()
    except ImportError:
        return reprex


venues_dispatcher: Dict[str, Callable] = {
    "gh": markdown,
    "so": markdown,
    "ds": markdown,
    "html": html,
    "py": py,
    "rtf": rtf,
    "slack": slack,
}


Venue = Enum("Venue", names={v.upper(): v for v in venues_dispatcher.keys()}, type=str)  # type: ignore
