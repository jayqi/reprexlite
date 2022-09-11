class ReprexliteException(Exception):
    """Base class for reprexlite exceptions."""


class InvalidInputPrefixesError(ValueError, ReprexliteException):
    pass


class MissingDependencyError(ImportError, ReprexliteException):
    pass


class PromptLengthMismatchError(ReprexliteException):
    pass


class NoPrefixMatchError(ValueError, ReprexliteException):
    pass
