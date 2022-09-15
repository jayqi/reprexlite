class ReprexliteException(Exception):
    """Base class for reprexlite exceptions."""


class InvalidInputPrefixesError(ValueError, ReprexliteException):
    pass


class InvalidParsingMethodError(ValueError, ReprexliteException):
    pass


class InvalidVenueError(ValueError, ReprexliteException):
    pass


class MissingDependencyError(ImportError, ReprexliteException):
    pass


class PromptLengthMismatchError(ReprexliteException):
    pass


class NoPrefixMatchError(ValueError, ReprexliteException):
    pass
