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
        raise  # pragma: no cover


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


class PrinterRegistry(Dict[str, Printer]):
    def register(self, venue: str):
        def registrar(fn: Printer):
            self[venue] = fn
            return fn

        return registrar


printer_registry = PrinterRegistry()
"""Registry of venue printers keyed by venue keywords."""


@printer_registry.register("ds")
@printer_registry.register("so")
@printer_registry.register("gh")
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


@printer_registry.register("htmlnocolor")
@printer_registry.register("html")
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


@printer_registry.register("py")
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
