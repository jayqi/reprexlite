class ReprexliteException(Exception):
    """Base class for reprexlite exceptions."""


class BlackNotFoundError(ModuleNotFoundError, ReprexliteException):
    """Raised when ipython cannot be found when using a black-dependent feature."""


class InvalidInputPrefixesError(ValueError, ReprexliteException):
    pass


class InvalidParsingMethodError(ValueError, ReprexliteException):
    pass


class InvalidVenueError(ValueError, ReprexliteException):
    pass


class IPythonNotFoundError(ModuleNotFoundError, ReprexliteException):
    """Raised when ipython cannot be found when using an IPython-dependent feature."""


class MissingDependencyError(ImportError, ReprexliteException):
    pass


class PromptLengthMismatchError(ReprexliteException):
    pass


class NoPrefixMatchError(ValueError, ReprexliteException):
    pass


class NotAFormatterError(TypeError, ReprexliteException):
    """Raised when registering a formatter that is not a subclass of the Formatter base class."""


class PygmentsNotFoundError(ModuleNotFoundError, ReprexliteException):
    """Raised when pygments cannot be found when using a pygments-dependent feature."""


class UnexpectedError(ReprexliteException):
    """Raised when an unexpected case happens."""
