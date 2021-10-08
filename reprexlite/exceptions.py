class ReprexliteException(Exception):
    """Base class for reprexlite exceptions."""


class PromptLengthMismatchError(ReprexliteException):
    pass


class MissingDependencyError(ImportError, ReprexliteException):
    pass
