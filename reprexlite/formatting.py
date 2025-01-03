from abc import ABC, abstractmethod
import dataclasses
from datetime import datetime
from textwrap import dedent
from typing import ClassVar, Dict, Optional, Type

from reprexlite.exceptions import NotAFormatterError, PygmentsNotFoundError
from reprexlite.session_info import SessionInfo
from reprexlite.version import __version__


@dataclasses.dataclass
class FormatterMetadata:
    example: Optional[str]
    venues: Dict[str, str] = dataclasses.field(default_factory=lambda: dict())


class Formatter(ABC):
    """Abstract base class for a reprex formatter. Concrete subclasses should implement the
    formatting logic appropriate to a specific venue for sharing. Call `str(...)` on an instance
    to return the formatted reprex.

    Attributes:
        default_advertise (bool): Whether to render reprexlite advertisement by default
        meta (FormatterMeta): Contains metadata for the formatter, such as label text and an
            example
    """

    default_advertise: ClassVar[bool] = True
    meta: ClassVar[FormatterMetadata]

    @classmethod
    @abstractmethod
    def format(
        cls, reprex_str: str, advertise: Optional[bool] = None, session_info: bool = False
    ) -> str:
        """Format a reprex string for a specific sharing venue.

        Args:
            reprex_str (str): String containing rendered reprex output.
            advertise (Optional[bool], optional): Whether to include the advertisement for
                reprexlite. Defaults to None, which uses a per-formatter default.
            session_info (bool, optional): Whether to include detailed session information.
                Defaults to False.

        Returns:
            str: String containing formatted reprex code. Ends with newline.
        """


formatter_registry: Dict[str, Type[Formatter]] = {}
"""Registry of formatters keyed by venue keywords."""


def register_formatter(venue: str, label: str):
    """Decorator that registers a formatter implementation.

    Args:
        venue (str): Venue keyword that formatter will be registered to.
        label (str): Short human-readable label explaining the venue.
    """

    def registrar(cls):
        global formatter_registry
        if not isinstance(cls, type) or not issubclass(cls, Formatter):
            raise NotAFormatterError("Only subclasses of Formatter can be registered.")
        formatter_registry[venue] = cls
        cls.meta.venues[venue] = label
        return cls

    return registrar


@register_formatter(venue="ds", label="Discourse (alias for 'gh')")
@register_formatter(venue="so", label="StackOverflow (alias for 'gh')")
@register_formatter(venue="gh", label="Github Flavored Markdown")
class GitHubFormatter(Formatter):
    """Formatter for rendering reprexes in GitHub Flavored Markdown."""

    default_advertise = True
    meta = FormatterMetadata(
        example=dedent(
            """\
            ```python
            2+2
            #> 4
            ```
            """
        )
    )

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
        return "\n".join(out) + "\n"


@register_formatter(venue="html", label="HTML")
class HtmlFormatter(Formatter):
    """Formatter for rendering reprexes in HTML. If optional dependency Pygments is
    available, the rendered HTML will have syntax highlighting for the Python code."""

    default_advertise = True
    meta = FormatterMetadata(
        example=dedent(
            """\
            <pre><code>2+2
            #> 4</code></pre>
            """
        )
    )

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
            out.append(Advertisement().html().strip())
        if session_info:
            out.append("<details><summary>Session Info</summary>")
            out.append(f"<pre><code>{SessionInfo()}</code></pre>")
            out.append("</details>")
        return "\n".join(out) + "\n"


@register_formatter(venue="py", label="Python script")
class PyScriptFormatter(Formatter):
    """Formatter for rendering reprexes as a Python script."""

    default_advertise = False
    meta = FormatterMetadata(
        example=dedent(
            """\
            2+2
            #> 4
            """
        )
    )

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
        return "\n".join(out) + "\n"


@register_formatter(venue="rtf", label="Rich Text Format")
class RtfFormatter(Formatter):
    """Formatter for rendering reprexes in Rich Text Format."""

    default_advertise = False
    meta = FormatterMetadata(example=None)

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
        except ModuleNotFoundError as e:
            if e.name == "pygments":
                raise PygmentsNotFoundError(
                    "Pygments is required for RTF output.", name="pygments"
                )
            else:
                raise

        out = str(reprex_str)
        if advertise:
            out += "\n\n" + Advertisement().text()
        if session_info:
            out += "\n\n" + str(SessionInfo())
        return highlight(out, PythonLexer(), RtfFormatter()) + "\n"


@register_formatter(venue="slack", label="Slack")
class SlackFormatter(Formatter):
    """Formatter for rendering reprexes as Slack markup."""

    default_advertise = False
    meta = FormatterMetadata(
        example=dedent(
            """\
            ```
            2+2
            #> 4
            ```
            """
        )
    )

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
        return "\n".join(out) + "\n"


class Advertisement:
    """Class for generating the advertisement note for reprexlite.

    Attributes:
        timestamp (str): Timestamp of instance instantiation
        version (str): Version of reprexlite
    """

    pkg = "reprexlite"
    url = "https://github.com/jayqi/reprexlite"

    def __init__(self):
        self.timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
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
