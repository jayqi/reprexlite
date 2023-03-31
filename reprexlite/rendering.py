import dataclasses
from datetime import datetime
from typing import TYPE_CHECKING, Dict, NamedTuple, Optional

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol  # type: ignore[assignment]

try:
    from pygments import highlight
    import pygments.formatters
    from pygments.lexers import PythonLexer

    PYGMENTS_IS_AVAILABLE = True
except ModuleNotFoundError as e:
    if e.name == "pygments":
        PYGMENTS_IS_AVAILABLE = False
    else:
        raise  # pragma: no cover


from reprexlite.exceptions import PygmentsNotFoundError
from reprexlite.session_info import SessionInfo
from reprexlite.version import __version__

if TYPE_CHECKING:
    from reprexlite.reprexes import Reprex


class Renderer(Protocol):
    """Callback protocol that defines the renderer callable type. A renderer callable
    should take a reprex and render it in the format for a particular venue."""

    def __call__(
        self, reprex: "Reprex", advertise: Optional[bool] = None, session_info: bool = False
    ) -> str:
        """Renders a reprex in the format for a particular venue.

        Args:
            reprex (Reprex): A reprex instance.
            advertise (Optional[bool], optional): Whether to include the advertisement for
                reprexlite. Defaults to None, which uses a per-renderer default.
            session_info (bool, optional): Whether to include detailed session information.
                Defaults to False.

        Returns:
            str: Rendered reprex. Always ends with newline.
        """


class RendererRegistration(NamedTuple):
    """Named tuple that contains a reference to a venue renderer callable and a human-readable
    label."""

    renderer: Renderer
    label: str


renderer_registry: Dict[str, RendererRegistration] = {}
"""Registry of reprex renderers keyed by venue keywords."""


def register_renderer(venue: str, label: str):
    """Decorator that registers a reprex renderer implementation to a venue keyword.

    Args:
        venue (str): Venue keyword that renderer will be registered to.
        label (str): Short human-readable label explaining the venue.
    """

    def registrar(fn: Renderer):
        global renderer_registry
        renderer_registry[venue] = RendererRegistration(renderer=fn, label=label)
        return fn

    return registrar


@register_renderer(venue="ds", label="Discourse (alias for 'gh')")
@register_renderer(venue="so", label="StackOverflow (alias for 'gh')")
@register_renderer(venue="gh", label="Github Flavored Markdown")
def render_github_flavored_markdown(
    reprex: "Reprex", advertise: Optional[bool] = None, session_info: bool = False
) -> str:
    """Render a reprex in GitHub Flavored Markdown.

    Args:
        reprex (Reprex): A reprex instance.
        advertise (Optional[bool], optional): Whether to include the advertisement for
            reprexlite. Defaults to None, which uses a per-renderer default.
        session_info (bool, optional): Whether to include detailed session information.
            Defaults to False.

    Returns:
        str: Rendered reprex. Always ends with newline.
    """
    if advertise is None:
        advertise = True
    out = []
    out.append("```python")
    out.append(str(reprex).strip())
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
class HtmlRenderer:
    """Render a reprex in HTML. Can use Pygments to add syntax highlighting to the rendered Python
    code block.

    Attributes:
        no_color (bool): Whether to disable syntax highlighting, regardless of whether Pygments is
            available.
        pygments_style (str): A valid Pygments style name.
    """

    no_color: bool
    pygments_style: str = "default"

    def __call__(
        self, reprex: "Reprex", advertise: Optional[bool] = None, session_info: bool = False
    ) -> str:
        """Render a reprex in HTML.

        Args:
            reprex (Reprex): A reprex instance.
            advertise (Optional[bool], optional): Whether to include the advertisement for
                reprexlite. Defaults to None, which uses a per-renderer default.
            session_info (bool, optional): Whether to include detailed session information.
                Defaults to False.

        Returns:
            str: Rendered reprex. Always ends with newline.
        """
        if advertise is None:
            advertise = True
        out = []

        if self.no_color or not PYGMENTS_IS_AVAILABLE:
            out.append(f'<pre><code class="language-python">{str(reprex).strip()}</code></pre>')
        else:
            formatter = pygments.formatters.HtmlFormatter(
                lineanchors=True, linenos=True, wrapcode=True, style=self.pygments_style
            )
            out.append(f"<style>{formatter.get_style_defs('.highlight')}</style>")
            out.append(highlight(str(reprex).strip(), PythonLexer(), formatter))

        if advertise:
            out.append(Advertisement().html().strip())
        if session_info:
            out.append("<details><summary>Session Info</summary>")
            out.append(f"<pre><code>{SessionInfo()}</code></pre>")
            out.append("</details>")
        return "\n".join(out) + "\n"


register_renderer(venue="html", label="HTML")(HtmlRenderer(no_color=False))
register_renderer(venue="htmlnocolor", label="HTML (No Color)")(HtmlRenderer(no_color=True))


@register_renderer(venue="py", label="Python script")
def render_python(
    reprex: "Reprex", advertise: Optional[bool] = None, session_info: bool = False
) -> str:
    """Renders a reprex as a Python script.

    Args:
        reprex (Reprex): A reprex instance.
        advertise (Optional[bool], optional): Whether to include the advertisement for
            reprexlite. Defaults to None, which uses a per-renderer default.
        session_info (bool, optional): Whether to include detailed session information.
            Defaults to False.

    Returns:
        str: Rendered reprex. Always ends with newline.
    """
    if advertise is None:
        advertise = False
    out = [str(reprex).strip()]
    if advertise:
        out.append("\n" + Advertisement().code_comment())
    if session_info:
        out.append("")
        sess_lines = str(SessionInfo()).split("\n")
        out.extend("# " + line for line in sess_lines)
    return "\n".join(out) + "\n"


@register_renderer(venue="rtf", label="Rich Text Format")
def render_rtf(
    reprex: "Reprex", advertise: Optional[bool] = None, session_info: bool = False
) -> str:
    """Renders a reprex in Rich Text Format (RTF).

    Args:
        reprex (Reprex): A reprex instance.
        advertise (Optional[bool], optional): Whether to include the advertisement for
            reprexlite. Defaults to None, which uses a per-renderer default.
        session_info (bool, optional): Whether to include detailed session information.
            Defaults to False.

    Returns:
        str: Rendered reprex. Always ends with newline.

    """
    if not PYGMENTS_IS_AVAILABLE:
        raise PygmentsNotFoundError("Pygments is required for RTF output.", name="pygments")

    if advertise is None:
        advertise = False

    out = str(reprex).strip()
    if advertise:
        out += "\n\n" + Advertisement().text()
    if session_info:
        out += "\n\n" + str(SessionInfo())
    return highlight(out, PythonLexer(), pygments.formatters.RtfFormatter()) + "\n"


@register_renderer(venue="slack", label="Slack")
def render_slack(
    reprex: "Reprex", advertise: Optional[bool] = None, session_info: bool = False
) -> str:
    """Renders a reprex in Slack markup.

    Args:
        reprex (Reprex): A reprex instance.
        advertise (Optional[bool], optional): Whether to include the advertisement for
            reprexlite. Defaults to None, which uses a per-renderer default.
        session_info (bool, optional): Whether to include detailed session information.
            Defaults to False.

    Returns:
        str: Rendered reprex. Always ends with newline.
    """
    if advertise is None:
        advertise = False
    out = []
    out.append("```")
    out.append(str(reprex).strip())
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
