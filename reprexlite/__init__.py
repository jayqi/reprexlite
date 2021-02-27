from reprexlite.reprex import reprex
from reprexlite.version import __version__  # noqa: F401

try:
    from reprexlite.ipython import load_ipython_extension  # noqa: F401
except ImportError:
    pass

__all__ = [
    "reprex",
]
