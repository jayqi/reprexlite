import dataclasses
from enum import Enum
import textwrap
from typing import Optional

from reprexlite.exceptions import PromptLengthMismatchError
from reprexlite.formatting import venues_dispatcher


@dataclasses.dataclass
class ReprexConfig:
    """Configuration for formatting and parsing

    Attributes:
    {{attributes}}
    """

    # Formatting
    venue: str = "gh"
    advertise: Optional[bool] = None
    session_info: bool = False
    style: bool = False
    prompt: str = ""
    continuation: str = ""
    comment: str = "#>"
    # Parsing
    parsing_method: str = "auto"
    input_prompt: Optional[str] = None
    input_continuation: Optional[str] = None
    input_comment: Optional[str] = None
    keep_old_results: bool = False

    def __post_init__(self):
        # Validate venue
        if self.venue not in venues_dispatcher:
            raise Exception
        # Validate prompt and continuation prefixes
        if len(self.prompt) != len(self.continuation):
            raise PromptLengthMismatchError(
                f"Primary prompt ('{self.prompt}') and continuation prompt "
                f"('{self.continuation}') must be equal lengths."
            )
        # Validate parsing method
        try:
            ParsingMethod(self.parsing_method)
        except ValueError:
            raise Exception

    @property
    def resolved_input_prompt(self):
        if self.input_prompt is not None:
            return self.input_prompt
        return self.prompt

    @property
    def resolved_input_continuation(self):
        if self.input_continuation is not None:
            return self.input_continuation
        return self.continuation

    @property
    def resolved_input_comment(self):
        if self.input_comment is not None:
            return self.input_comment
        return self.comment


class ParsingMethod(str, Enum):
    AUTO = "auto"
    DECLARED = "declared"


CONFIG_DOCS = {
    # Formatting
    "venue": "Output format appropriate to the venue where you plan to share this code.",
    "advertise": (
        "Whether to include footer that credits reprexlite. "
        "If unspecified, will depend on specified venue's default."
    ),
    "session_info": "Include details about session and installed packages.",
    "style": "Autoformat code with black. Requires black to be installed.",
    "prompt": "Prefix to use as primary prompt for code lines.",
    "continuation": "Prefix to use as secondary prompt for continued code lines.",
    "comment": "Comment prefix to use for results returned by expressions.",
    # Parsing
    "parsing_method": (
        "Method for parsing input. 'auto' will appropriate detect default "
        "reprex-style input or standard doctest-style input. 'declared'"
    ),
    "input_prompt": (
        "Prefix for primary prompts when parsing input. Only used if parsing method "
        "is 'declared'."
    ),
    "input_continuation": (
        "Prefix for continuation prompts when parsing input. Only used if "
        "parsing method is 'declared'."
    ),
    "input_comment": (
        "Prefix for result lines when parsing input. Only used if parsing method is 'declared'."
    ),
    "keep_old_results": (
        "Keep any existing evaluation results detected in input as comments. If "
        "false, these will be stripped."
    ),
}


def format_args_google_style():
    docs = []
    for field in dataclasses.fields(ReprexConfig):
        field_name = field.name
        try:
            field_type = field.type.__name__
        except AttributeError:
            field_type = str(field.type)
        docs.extend(
            textwrap.wrap(
                f"{field_name} ({field_type}): {CONFIG_DOCS[field_name]}",
                width=99,
                initial_indent=" " * 8,
                subsequent_indent=" " * 12,
            )
        )
    return "\n".join(docs)[4:]


if ReprexConfig.__doc__:
    ReprexConfig.__doc__ = ReprexConfig.__doc__.replace("{{args}}", format_args_google_style())
