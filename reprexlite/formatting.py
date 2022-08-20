from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Optional, Type

from reprexlite.session_info import SessionInfo
from reprexlite.version import __version__


class Formatter(ABC):
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

    @classmethod
    @abstractmethod
    def format(
        cls, reprex_str: str, advertise: Optional[bool] = None, session_info: bool = False
    ) -> str:
        pass


venues_dispatcher: Dict[str, Type[Formatter]] = {}
"""Mapping from venue keywords to their Formatter implementation."""


def register_formatter(venue: str):
    def registrar(cls):
        global venues_dispatcher
        if not isinstance(cls, type) or not issubclass(cls, Formatter):
            raise Exception
        venues_dispatcher[venue] = cls
        return cls

    return registrar


@register_formatter(venue="gh")
@register_formatter(venue="so")
@register_formatter(venue="ds")
class GitHubFormatter(Formatter):
    """Concrete implementation for rendering reprexes in GitHub Flavored Markdown."""

    default_advertise: bool = True

    @classmethod
    def format(
        cls, reprex_str: str, advertise: Optional[bool] = None, session_info: bool = False
    ) -> str:
        if advertise is None:
            advertise = cls.default_advertise
        out = []
        out.append("```python")
        out.append(reprex_str)
        out.append("```")
        if advertise:
            out.append("\n" + Advertisement().markdown())
        if session_info:
            out.append("\n<details><summary>Session Info</summary>")
            out.append("```text")
            out.append(str(SessionInfo()))
            out.append("```")
            out.append("</details>")
        return "\n".join(out)


@register_formatter(venue="html")
class HtmlFormatter(Formatter):
    """Concrete implementation for rendering reprexes in HTML. If optional dependency Pygments is
    available, the rendered HTML will have syntax highlighting for the Python code."""

    default_advertise: bool = True

    @classmethod
    def format(
        cls, reprex_str: str, advertise: Optional[bool] = None, session_info: bool = False
    ) -> str:
        if advertise is None:
            advertise = cls.default_advertise
        out = []
        try:
            from pygments import highlight
            from pygments.formatters import HtmlFormatter
            from pygments.lexers import PythonLexer

            formatter = HtmlFormatter(
                style="friendly", lineanchors=True, linenos=True, wrapcode=True
            )
            out.append(f"<style>{formatter.get_style_defs('.highlight')}</style>")
            out.append(highlight(str(reprex_str), PythonLexer(), formatter))
        except ImportError:
            out.append(f"<pre><code>{reprex_str}</code></pre>")

        if advertise:
            out.append(Advertisement().html())
        if session_info:
            out.append("<details><summary>Session Info</summary>")
            out.append(f"<pre><code>{SessionInfo()}</code></pre>")
            out.append("</details>")
        return "\n".join(out)


@register_formatter(venue="py")
class PyScriptFormatter(Formatter):
    """Concrete implementation for rendering reprexes as a Python script."""

    default_advertise: bool = False

    @classmethod
    def format(
        cls, reprex_str: str, advertise: Optional[bool] = None, session_info: bool = False
    ) -> str:
        if advertise is None:
            advertise = cls.default_advertise
        out = [str(reprex_str)]
        if advertise:
            out.append("\n" + Advertisement().code_comment())
        if session_info:
            out.append("")
            sess_lines = str(SessionInfo()).split("\n")
            out.extend("# " + line for line in sess_lines)
        return "\n".join(out)


@register_formatter(venue="rtf")
class RtfFormatter(Formatter):
    """Concrete implementation for rendering reprexes in Rich Text Format."""

    default_advertise: bool = False

    @classmethod
    def format(
        cls, reprex_str: str, advertise: Optional[bool] = None, session_info: bool = False
    ) -> str:
        if advertise is None:
            advertise = cls.default_advertise
        try:
            from pygments import highlight
            from pygments.formatters import RtfFormatter
            from pygments.lexers import PythonLexer
        except ImportError:
            raise ImportError("Pygments is required for RTF output.")

        out = str(reprex_str)
        if advertise:
            out += "\n\n" + Advertisement().text()
        if session_info:
            out += "\n\n" + str(SessionInfo())
        return highlight(out, PythonLexer(), RtfFormatter())


@register_formatter(venue="slack")
class SlackFormatter(Formatter):
    """Concrete implementation for rendering reprexes as Slack markup."""

    default_advertise: bool = False

    @classmethod
    def format(
        cls, reprex_str: str, advertise: Optional[bool] = None, session_info: bool = False
    ) -> str:
        if advertise is None:
            advertise = cls.default_advertise
        out = []
        out.append("```")
        out.append(str(reprex_str))
        out.append("```")
        if advertise:
            out.append("\n" + Advertisement().text())
        if session_info:
            out.append("\n```")
            out.append(str(SessionInfo()))
            out.append("```")
        return "\n".join(out)


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