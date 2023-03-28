from typing import Dict

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol  # type: ignore[assignment]


try:
    from rich.console import Console
    from rich.syntax import Syntax

    RICH_IS_AVAILABLE = True
    console = Console(soft_wrap=True)
except ModuleNotFoundError as e:
    if e.name == "rich":
        RICH_IS_AVAILABLE = False
    else:
        raise


from reprexlite.exceptions import RichNotFoundError


class Printer(Protocol):
    """Callback protocol for a printer callable type. A printer callable should print a given
    venue-formatted reprex to stdout, potentially with terminal coloring."""

    def __call__(self, formatted_reprex: str, **kwargs):
        """Print given venue-formatted reprex to stdout.

        Args:
            formatted_reprex (str): Formatted reprex.
            **kwargs: Arguments passed to print().
        """


printer_registry: Dict[str, Printer] = {}
"""Registry of venue printers keyed by venue keywords."""


def register_printer(venue: str):
    def registrar(fn: Printer):
        global formatter_registry
        printer_registry[venue] = fn
        return fn

    return registrar


@register_printer("ds")
@register_printer("so")
@register_printer("gh")
def print_markdown(formatted_reprex: str, **kwargs):
    """Print a formatted markdown reprex using rich.

    Args:
        formatted_reprex (str): Formatted reprex.
        **kwargs: Arguments passed to rich's Console.print.
    """
    if RICH_IS_AVAILABLE:
        console.print(Syntax(formatted_reprex, "markdown", theme="ansi_dark"), **kwargs)
    else:
        raise RichNotFoundError


@register_printer("htmlnocolor")
@register_printer("html")
def print_html(formatted_reprex: str, **kwargs):
    """Print a formatted HTML reprex using rich.

    Args:
        formatted_reprex (str): Formatted reprex.
        **kwargs: Arguments passed to rich's Console.print.
    """
    if RICH_IS_AVAILABLE:
        console.print(Syntax(formatted_reprex, "html", theme="ansi_dark"), **kwargs)
    else:
        raise RichNotFoundError


@register_printer("py")
def print_python_code(formatted_reprex: str, **kwargs):
    """Print a formatted Python code reprex using rich.

    Args:
        formatted_reprex (str): Formatted reprex.
        **kwargs: Arguments passed to rich's Console.print.
    """
    if RICH_IS_AVAILABLE:
        console.print(Syntax(formatted_reprex, "python", theme="ansi_dark"), **kwargs)
    else:
        raise RichNotFoundError
