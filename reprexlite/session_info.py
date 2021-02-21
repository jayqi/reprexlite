import platform
import sys
from typing import List, Tuple

if sys.version_info[:2] >= (3, 8):
    import importlib.metadata as importlib_metadata
else:
    import importlib_metadata


class SessionInfo:
    """Class for pretty-formatting Python session info. Includes details about your Python version,
    your operating system, and the Python packages installed in your current environment.

    Attributes:
        python_version (str): Python version for current session
        python_build_date (str): Date
        os (str): OS information for current session
        packages (List[Package]): List of Python packages installed in current virtual environment.
    """

    def __init__(self):
        self.python_version: str = platform.python_version()
        self.python_build_date: str = platform.python_build()[1]

        self.os: str = platform.platform()
        self.packages: List[Package] = [
            Package(distr) for distr in importlib_metadata.Distribution.discover()
        ]

    def __str__(self):
        lines = ["-- Session Info --" + "-" * 60]
        lines += tabulate(
            [
                ("version", f"Python {self.python_version} ({self.python_build_date})"),
                ("os", self.os),
            ]
        )
        lines += ["-- Packages --" + "-" * 64]
        lines += tabulate([(pkg.name, pkg.version) for pkg in sorted(self.packages)])
        return "\n".join(lines).strip()


class Package:
    """Interface for adapting [`importlib.metadata.Distribution`](https://docs.python.org/3/library/importlib.metadata.html#distributions)
    instances for introspection by [`SessionInfo`][reprexlite.session_info.SessionInfo].
    """

    def __init__(self, distribution: importlib_metadata.Distribution):
        self.distribution = distribution

    @property
    def name(self) -> str:
        return self.distribution.metadata["Name"]

    @property
    def version(self) -> str:
        return self.distribution.version

    def __lt__(self, other) -> bool:
        if not isinstance(other, Package):
            raise ValueError
        return self.name < other.name


def tabulate(rows: List[Tuple[str, str]]) -> List[str]:
    """Utility function for printing a two-column table as text with whitespace padding.

    Args:
        rows (List[Tuple[str, str]]): Rows of table as tuples of (left cell, right cell)

    Returns:
        Rows of table formatted as strings with whitespace padding
    """
    left_max = max(len(row[0]) for row in rows)
    out = []
    for left, right in rows:
        padding = (left_max + 1 - len(left)) * " "
        out.append(left + padding + right)
    return out
