from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Dict, Optional, Type

from reprexlite.code import CodeBlock
from reprexlite.session_info import SessionInfo
from reprexlite.version import __version__


class Reprex(ABC):
    """Abstract base class for a reprex instance. Concrete subclasses should implement the
    formatting logic appropriate to a specific venue for sharing. Call `str(...)` on an instance
    to return the formatted reprex.

    Attributes:
        code_block (CodeBlock): instance of [`CodeBlock`][reprexlite.code.CodeBlock]
        advertise (bool): whether to render reprexlite advertisement
        session_info (bool): whether to render session info
    """

    default_advertise: bool
    """Default for whether to include reprexlite advertisement for this venue format."""

    def __init__(
        self, code_block: CodeBlock, advertise: Optional[bool] = None, session_info: bool = False
    ):
        self.code_block: CodeBlock = code_block
        self.advertise: bool = self.default_advertise if advertise is None else advertise
        self.session_info: bool = session_info

    @abstractmethod
    def __str__(self) -> str:  # pragma: no cover
        pass


class GitHubReprex(Reprex):
    """Concrete implementation for rendering reprexes in GitHub Flavored Markdown."""

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
    """Concrete implementation for rendering reprexes in HTML. If optional dependency Pygments is
    available, the rendered HTML will have syntax highlighting for the Python code."""

    default_advertise: bool = True

    def __str__(self) -> str:
        out = []
        try:
            from pygments import highlight
            from pygments.formatters import HtmlFormatter
            from pygments.lexers import PythonLexer

            formatter = HtmlFormatter(
                style="friendly", lineanchors=True, linenos=True, wrapcode=True
            )
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
    """Concrete implementation for rendering reprexes as a Python script."""

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
    """Concrete implementation for rendering reprexes in Rich Text Format."""

    default_advertise: bool = False

    def __str__(self) -> str:
        try:
            from pygments import highlight
            from pygments.formatters import RtfFormatter
            from pygments.lexers import PythonLexer
        except ImportError:
            raise ImportError("Pygments is required for RTF output.")

        out = str(self.code_block)
        if self.advertise:
            out += "\n\n" + Advertisement().text()
        if self.session_info:
            out += "\n\n" + str(SessionInfo())
        return highlight(out, PythonLexer(), RtfFormatter())


class SlackReprex(Reprex):
    """Concrete implementation for rendering reprexes as Slack markup."""

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


venues_dispatcher: Dict[str, Type[Reprex]] = {
    "gh": GitHubReprex,
    "so": GitHubReprex,
    "ds": GitHubReprex,
    "html": HtmlReprex,
    "py": PyScriptReprex,
    "rtf": RtfReprex,
    "slack": SlackReprex,
}
"""Mapping from venue keywords to their Reprex implementation."""


Venue = Enum("Venue", names={v.upper(): v for v in venues_dispatcher.keys()}, type=str)  # type: ignore
Venue.__doc__ = """Enum for valid venue options."""


class Advertisement:
    """Class for generating the advertisement note for reprexlite.

    Attributes:
        timestamp (str): Timestamp of instance instantiation
        version (str): Version of reprexlite
    """

    pkg = "reprexlite"
    url = "https://github.com/jayqi/reprexlite"

    def __init__(self):
        self.timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
        self.version = f"v{__version__}"

    def markdown(self) -> str:
        """Render reprexlite advertisement in GitHub Flavored Markdown."""
        return f"<sup>Created at {self.timestamp} by [{self.pkg}]({self.url}) {self.version}</sup>"

    def html(self) -> str:
        """Render reprexlite advertisement in HTML."""
        return (
            f"<p><sup>Created at {self.timestamp} by "
            f'<a href="{self.url}">{self.pkg}</a> {self.version}</sup></p>'
        )

    def code_comment(self) -> str:
        """Render reprexlite advertisement as a comment in Python code."""
        return f"# {self.text()}"

    def text(self) -> str:
        """Render reprexlite advertisement in plain text."""
        return f"Created at {self.timestamp} by {self.pkg} {self.version} <{self.url}>"
