import pytest

from reprexlite.config import ReprexConfig
from reprexlite.exceptions import (
    InvalidParsingMethodError,
    InvalidVenueError,
    PromptLengthMismatchError,
)


def test_prompt_length_mismatch():
    with pytest.raises(PromptLengthMismatchError):
        ReprexConfig(prompt="123", continuation="1234")


def test_invalid_parsing_method():
    with pytest.raises(InvalidParsingMethodError):
        ReprexConfig(parsing_method="???")


def test_invalid_venue():
    with pytest.raises(InvalidVenueError):
        ReprexConfig(venue="carnegie_hall")
