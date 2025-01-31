from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional, Protocol, Type

from reprexlite.config import ReprexConfig, Venue
from reprexlite.exceptions import PygmentsNotFoundError
from reprexlite.session_info import SessionInfo
from reprexlite.version import __version__


class Formatter(Protocol):
    def __call__(self, reprex_str: str, config: Optional[ReprexConfig] = None) -> str: ...


@dataclass
class FormatterRegistration:
    fn: Formatter
    label: str


class FormatterRegistry:
    """Registry of formatters keyed by venue keywords."""

    _registry: Dict[str, FormatterRegistration] = {}

    def __getitem__(self, key: Venue) -> FormatterRegistration:
        return self._registry[Venue(key)]

    def __contains__(self, key: Venue) -> bool:
        return Venue(key) in self._registry

    def items(self):
        return self._registry.items()

    def keys(self):
        return self._registry.keys()

    def values(self):
        return self._registry.values()

    def register(self, venue: Venue, label: str):
        """Decorator that registers a formatter implementation.

        Args:
            venue (str): Venue keyword that formatter will be registered to.
            label (str): Short human-readable label explaining the venue.
        """

        def _register(fn: Formatter):
            self._registry[Venue(venue)] = FormatterRegistration(fn=fn, label=label)
            return fn

        return _register


formatter_registry = FormatterRegistry()


@formatter_registry.register(venue=Venue.DS, label=f"Discourse (alias for '{Venue.GH.value}')")
@formatter_registry.register(venue=Venue.SO, label=f"StackOverflow (alias for '{Venue.GH.value}')")
@formatter_registry.register(venue=Venue.GH, label="Github Flavored Markdown")
def format_as_markdown(
    reprex_str: str,
    config: Optional[ReprexConfig] = None,
) -> str:
    """
    Format a rendered reprex reprex as a GitHub-Flavored Markdown code block. By default, includes
    a footer that credits reprexlite.

    Args:
        reprex_str (str): The reprex string to render.
        config (Optional[ReprexConfig]): Configuration for the reprex. Defaults to None.

    Returns:
        str: The rendered reprex

    Example:
        ```python
        2+2
        #> 4
        ```
    """
    if config is None:
        config = ReprexConfig()
    advertise = config.advertise if config.advertise is not None else True
    out = []
    out.append("```python")
    out.append(reprex_str)
    out.append("```")
    if advertise:
        out.append("\n" + Advertisement().markdown())
    if config.session_info:
        out.append("\n<details><summary>Session Info</summary>")
        out.append("```text")
        out.append(str(SessionInfo()))
        out.append("```")
        out.append("</details>")
    return "\n".join(out) + "\n"


@formatter_registry.register(venue=Venue.HTML, label="HTML")
def format_as_html(reprex_str: str, config: Optional[ReprexConfig] = None) -> str:
    """Format a rendered reprex reprex as an HTML code block. If optional dependency Pygments is
    available, the rendered HTML will have syntax highlighting for the Python code. By default,
    includes a footer that credits reprexlite.

    Args:
        reprex_str (str): The reprex string to render.
        config (Optional[ReprexConfig]): Configuration for the reprex. Defaults to None.

    Returns:
        str: The rendered reprex

    Example:
        <pre><code>2+2
        #> 4</code></pre>
    """
    if config is None:
        config = ReprexConfig()
    advertise = config.advertise if config.advertise is not None else True
    out = []
    try:
        from pygments import highlight
        from pygments.formatters import HtmlFormatter
        from pygments.lexers import PythonLexer

        formatter = HtmlFormatter(style="friendly", lineanchors=True, linenos=True, wrapcode=True)
        out.append(f"<style>{formatter.get_style_defs('.highlight')}</style>")
        out.append(highlight(str(reprex_str), PythonLexer(), formatter))
    except ImportError:
        out.append(f"<pre><code>{reprex_str}</code></pre>")

    if advertise:
        out.append(Advertisement().html().strip())
    if config.session_info:
        out.append("<details><summary>Session Info</summary>")
        out.append(f"<pre><code>{SessionInfo()}</code></pre>")
        out.append("</details>")
    return "\n".join(out) + "\n"


@formatter_registry.register(venue=Venue.PY, label="Python script")
def format_as_python_script(reprex_str: str, config: Optional[ReprexConfig] = None) -> str:
    """Format a rendered reprex reprex as a Python script.

    Args:
        reprex_str (str): The reprex string to render.
        config (Optional[ReprexConfig]): Configuration for the reprex. Defaults to None.

    Returns:
        str: The rendered reprex

    Example:
        2+2
        #> 4
    """
    if config is None:
        config = ReprexConfig()
    advertise = config.advertise if config.advertise is not None else False
    out = [str(reprex_str)]
    if advertise:
        out.append("\n" + Advertisement().code_comment())
    if config.session_info:
        out.append("")
        sess_lines = str(SessionInfo()).split("\n")
        out.extend("# " + line for line in sess_lines)
    return "\n".join(out) + "\n"


@formatter_registry.register(venue=Venue.RTF, label="Rich Text Format")
def format_as_rtf(reprex_str: str, config: Optional[ReprexConfig] = None) -> str:
    """Format a rendered reprex reprex as a Rich Text Format (RTF) document. Requires dependency
    Pygments."""
    if config is None:
        config = ReprexConfig()
    advertise = config.advertise if config.advertise is not None else False
    try:
        from pygments import highlight
        from pygments.formatters import RtfFormatter
        from pygments.lexers import PythonLexer
    except ModuleNotFoundError as e:
        if e.name == "pygments":
            raise PygmentsNotFoundError("Pygments is required for RTF output.", name="pygments")
        else:
            raise

    out = str(reprex_str)
    if advertise:
        out += "\n\n" + Advertisement().text()
    if config.session_info:
        out += "\n\n" + str(SessionInfo())
    return highlight(out, PythonLexer(), RtfFormatter()) + "\n"


@formatter_registry.register(venue=Venue.SLACK, label="Slack")
def format_for_slack(reprex_str: str, config: Optional[ReprexConfig] = None) -> str:
    """Format a rendered reprex as Slack markup.

    Args:
        reprex_str (str): The reprex string to render.
        config (Optional[ReprexConfig]): Configuration for the reprex. Defaults to None.

    Returns:
        str: The rendered reprex

    Example:
        ```
        2+2
        #> 4
        ```
    """
    if config is None:
        config = ReprexConfig()
    advertise = config.advertise if config.advertise is not None else False
    out = []
    out.append("```")
    out.append(str(reprex_str))
    out.append("```")
    if advertise:
        out.append("\n" + Advertisement().text())
    if config.session_info:
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
