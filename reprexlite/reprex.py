from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Callable, Dict, Optional

from reprexlite.code import CodeBlock
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


class Reprex(ABC):
    default_advertise: bool

    def __init__(
        self, code_block: CodeBlock, advertise: Optional[bool] = None, session_info: bool = False
    ):
        self.code_block = code_block
        self.advertise = self.default_advertise if advertise is None else advertise
        self.session_info = session_info

    @abstractmethod
    def __str__(self) -> str:
        pass


class GitHubReprex(Reprex):
    default_advertise: bool = True

    def __str__(self) -> str:
        out = []
        out.append("```python")
        out.append(str(self.code_block))
        out.append("```")
        if self.advertise:
            out.append("\n" + Advertisement().markdown())
        if self.session_info:
            out.append("\n<details><summary>Session Info</summary>")
            out.append("```text")
            out.append(str(SessionInfo()))
            out.append("```")
            out.append("</details>")
        return "\n".join(out)


class HtmlReprex(Reprex):
    default_advertise: bool = True

    def __str__(self) -> str:
        out = []
        try:
            from pygments import highlight
            from pygments.lexers import PythonLexer
            from pygments.formatters import HtmlFormatter

            formatter = HtmlFormatter()
            out.append(f"<style>{formatter.get_style_defs('.highlight')}</style>")
            out.append(highlight(str(self.code_block), PythonLexer(), formatter))
        except ImportError:
            out.append(f"<pre><code>{self.code_block}</code></pre>")

        if self.advertise:
            out.append(Advertisement().html())
        if self.session_info:
            out.append("<details><summary>Session Info</summary>")
            out.append(f"<pre><code>{SessionInfo()}</code></pre>")
            out.append("</details>")
        return "\n".join(out)


class PyScriptReprex(Reprex):
    default_advertise: bool = False

    def __str__(self) -> str:
        out = [str(self.code_block)]
        if self.advertise:
            out.append("\n" + Advertisement().code_comment())
        if self.session_info:
            out.append("")
            sess_lines = str(SessionInfo()).split("\n")
            out.extend("# " + line for line in sess_lines)
        return "\n".join(out)


class RtfReprex(Reprex):
    default_advertise: bool = False

    def __str__(self) -> str:
        try:
            from pygments import highlight
            from pygments.lexers import PythonLexer
            from pygments.formatters import RtfFormatter
        except ImportError:
            raise ImportError("Pygments is required for RTF output.")

        out = str(self.code_block)
        if self.advertise:
            out += "\n\n" + Advertisement().text()
        if self.session_info:
            out += "\n\n" + SessionInfo()
        return highlight(out, PythonLexer(), RtfFormatter())


class SlackReprex(Reprex):
    default_advertise: bool = False

    def __str__(self):
        out = []
        out.append("```")
        out.append(str(self.code_block))
        out.append("```")
        if self.advertise:
            out.append("\n" + Advertisement().text())
        if self.session_info:
            out.append("\n```")
            out.append(str(SessionInfo()))
            out.append("```")
        return "\n".join(out)


venues_dispatcher: Dict[str, Callable] = {
    "gh": GitHubReprex,
    "so": GitHubReprex,
    "ds": GitHubReprex,
    "html": HtmlReprex,
    "py": PyScriptReprex,
    "rtf": RtfReprex,
    "slack": SlackReprex,
}


Venue = Enum("Venue", names={v.upper(): v for v in venues_dispatcher.keys()}, type=str)  # type: ignore


def reprex(
    input: str,
    outfile: Optional[Path] = None,
    venue="gh",
    advertise: Optional[bool] = None,
    session_info: bool = False,
    style: bool = False,
    comment: str = "#>",
    print_=True,
    terminal=False,
) -> Optional[Reprex]:
    if outfile or venue in ["html", "rtf"]:
        # Don't screw output file or lexing for HTML and RTF
        terminal = False
    code_block = CodeBlock(input, style=style, comment=comment, terminal=terminal)

    reprex = venues_dispatcher[venue](
        code_block=code_block, advertise=advertise, session_info=session_info
    )
    if outfile is not None:
        with outfile.open("w") as fp:
            fp.write(str(reprex) + "\n")
        return
    if print_:
        print(reprex)
        return
    return reprex
