from reprexlite.reprex import reprex
from reprexlite.version import __version__  # noqa: F401

try:
    import reprexlite.ipython  # noqa: F401
except (ImportError, NameError):
    pass

__all__ = [
    "reprex",
]
