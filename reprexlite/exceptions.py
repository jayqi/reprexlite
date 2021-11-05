class ReprexliteException(Exception):
    """Base class for reprexlite exceptions."""


class InvalidInputPrefixes(ValueError, ReprexliteException):
    pass


class MissingDependencyError(ImportError, ReprexliteException):
    pass


class PromptLengthMismatchError(ReprexliteException):
    pass
