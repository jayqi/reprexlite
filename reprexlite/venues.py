from datetime import datetime
from enum import Enum
from typing import Callable, Dict, TYPE_CHECKING, Union

from reprexlite.version import __version__

if TYPE_CHECKING:
    from reprexlite.reprex import Reprex


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


def markdown(reprex: Union["Reprex", str], advertise: bool = True) -> str:
    out = "\n".join(
        [
            "```python",
            str(reprex),
            "```\n",
        ]
    )
    if advertise:
        out += "\n" + Advertisement().markdown() + "\n"
    return out


def html(reprex: Union["Reprex", str], advertise: bool = True) -> str:
    try:
        from pygments import highlight
        from pygments.lexers import PythonLexer
        from pygments.formatters import HtmlFormatter
    except ImportError:
        raise ImportError("Pygments is required for HTML output.")

    formatter = HtmlFormatter()
    style = f"<style>{formatter.get_style_defs('.highlight')}</style>"
    code = highlight(str(reprex), PythonLexer(), formatter)
    ad = "\n" + Advertisement().html() if advertise else ""
    return style + code + ad


def py(reprex: Union["Reprex", str], advertise: bool = False) -> str:
    ad = "\n\n" + Advertisement().code_comment() if advertise else ""
    return str(reprex) + ad


def rtf(reprex: Union["Reprex", str], advertise: bool = False) -> str:
    try:
        from pygments import highlight
        from pygments.lexers import PythonLexer
        from pygments.formatters import RtfFormatter
    except ImportError:
        raise ImportError("Pygments is required for RTF output.")
    out = str(reprex)
    if advertise:
        out += "\n\n" + Advertisement().text()
    return highlight(out, PythonLexer(), RtfFormatter())


def slack(reprex: Union["Reprex", str], advertise: bool = False) -> str:
    ad = "\n" + Advertisement().text() if advertise else ""
    return "\n".join(["```", str(reprex), "```"]) + ad


def display_terminal(reprex: "Reprex"):
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
