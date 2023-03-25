import dataclasses
from datetime import datetime
from typing import Dict, Optional

try:
    from typing import Protocol, runtime_checkable
except ImportError:
    from typing_extensions import Protocol, runtime_checkable

try:
    from pygments import highlight
    import pygments.formatters
    from pygments.lexers import PythonLexer

    PYGMENTS_AVAILABLE = True
except ModuleNotFoundError as e:
    if e.name == "pygments":
        PYGMENTS_AVAILABLE = False
    else:
        raise

from reprexlite.exceptions import NotAFormatterError, PygmentsNotFoundError
from reprexlite.session_info import SessionInfo
from reprexlite.version import __version__


@dataclasses.dataclass
class FormatterMetadata:
    example: Optional[str]
    venues: Dict[str, str] = dataclasses.field(default_factory=lambda: dict())


@runtime_checkable
class Formatter(Protocol):
    def __call__(
        self, reprex_str: str, advertise: Optional[bool] = None, session_info: bool = False
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


formatter_registry: Dict[str, Formatter] = {}
"""Registry of formatters keyed by venue keywords."""


def register_formatter(venue: str, label: str):
    """Decorator that registers a formatter implementation.

    Args:
        venue (str): Venue keyword that formatter will be registered to.
        label (str): Short human-readable label explaining the venue.
    """

    def registrar(fn):
        global formatter_registry
        if not isinstance(fn, Formatter):
            raise NotAFormatterError("Only subclasses of Formatter can be registered.")
        formatter_registry[venue] = {"formatter": fn, "label": label}
        return fn

    return registrar


@register_formatter(venue="ds", label="Discourse (alias for 'gh')")
@register_formatter(venue="so", label="StackOverflow (alias for 'gh')")
@register_formatter(venue="gh", label="Github Flavored Markdown")
def format_github_flavored_markdown(
    reprex_str: str, advertise: Optional[bool] = None, session_info: bool = False
) -> str:
    """Formatter for rendering reprexes in GitHub Flavored Markdown.

    Args:
        reprex_str (str): String containing rendered reprex output.
        advertise (Optional[bool], optional): Whether to include the advertisement for
            reprexlite. Defaults to None, which uses a per-formatter default.
        session_info (bool, optional): Whether to include detailed session information.
            Defaults to False.

    Returns:
        str: String containing formatted reprex code. Ends with newline.
    """
    if advertise is None:
        advertise = True
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


@dataclasses.dataclass
class HtmlFormatter:
    """Formatter for rendering reprexes in HTML. If optional dependency Pygments is
    available, the rendered HTML will have syntax highlighting for the Python code."""

    no_color: bool

    def __call__(
        self, reprex_str: str, advertise: Optional[bool] = None, session_info: bool = False
    ) -> str:
        if advertise is None:
            advertise = True
        out = []

        if self.no_color or not PYGMENTS_AVAILABLE:
            out.append(f'<pre><code class="language-python">{reprex_str}</code></pre>')
        else:
            formatter = pygments.formatters.HtmlFormatter(
                lineanchors=True, linenos=True, wrapcode=True
            )
            out.append(f"<style>{formatter.get_style_defs('.highlight')}</style>")
            out.append(highlight(str(reprex_str), PythonLexer(), formatter))

        if advertise:
            out.append(Advertisement().html().strip())
        if session_info:
            out.append("<details><summary>Session Info</summary>")
            out.append(f"<pre><code>{SessionInfo()}</code></pre>")
            out.append("</details>")
        return "\n".join(out) + "\n"


register_formatter(venue="html", label="HTML")(HtmlFormatter(no_color=False))
register_formatter(venue="htmlnocolor", label="HTML (No Color)")(HtmlFormatter(no_color=True))


@register_formatter(venue="py", label="Python script")
def format_python(
    reprex_str: str, advertise: Optional[bool] = None, session_info: bool = False
) -> str:
    if advertise is None:
        advertise = False
    out = [str(reprex_str)]
    if advertise:
        out.append("\n" + Advertisement().code_comment())
    if session_info:
        out.append("")
        sess_lines = str(SessionInfo()).split("\n")
        out.extend("# " + line for line in sess_lines)
    return "\n".join(out) + "\n"


@register_formatter(venue="rtf", label="Rich Text Format")
def format_rtf(
    reprex_str: str, advertise: Optional[bool] = None, session_info: bool = False
) -> str:
    if not PYGMENTS_AVAILABLE:
        raise PygmentsNotFoundError("Pygments is required for RTF output.", name="pygments")

    if advertise is None:
        advertise = False

    out = str(reprex_str)
    if advertise:
        out += "\n\n" + Advertisement().text()
    if session_info:
        out += "\n\n" + str(SessionInfo())
    return highlight(out, PythonLexer(), pygments.formatters.RtfFormatter()) + "\n"


@register_formatter(venue="slack", label="Slack")
def format_slack(
    reprex_str: str, advertise: Optional[bool] = None, session_info: bool = False
) -> str:
    if advertise is None:
        advertise = False
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
