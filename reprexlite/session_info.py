import platform
import sys
from typing import List, Tuple

if sys.version_info[:2] >= (3, 8):
    import importlib.metadata as importlib_metadata
else:
    import importlib_metadata


class SessionInfo:
    def __init__(self):
        self.python_version = platform.python_version()
        self.python_build_date = platform.python_build()[1]

        self.os = platform.platform()
        self.packages = [Package(distr) for distr in importlib_metadata.Distribution.discover()]

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
    left_max = max(len(row[0]) for row in rows)
    out = []
    for left, right in rows:
        padding = (left_max + 1 - len(left)) * " "
        out.append(left + padding + right)
    return out
