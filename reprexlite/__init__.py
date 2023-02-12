from reprexlite.reprexes import Reprex, ReprexConfig, reprex
from reprexlite.version import __version__

try:
    from reprexlite.ipython import load_ipython_extension  # noqa: F401
except ImportError:
    pass

__all__ = [
    "Reprex",
    "ReprexConfig",
    "reprex",
]

__version__
