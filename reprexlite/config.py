from dataclasses import dataclass
from enum import Enum
from typing import Annotated, Optional

from cyclopts import Parameter

from reprexlite.exceptions import (
    InvalidParsingMethodError,
    InvalidVenueError,
    PromptLengthMismatchError,
)


class ParsingMethod(str, Enum):
    """Methods for parsing input strings.

    Attributes:
        AUTO (str): Automatically identify reprex-style or doctest-style input.
        DECLARED (str): Use configured values for parsing.
    """

    AUTO = "auto"
    DECLARED = "declared"


class Venue(str, Enum):
    """Enum for specifying the output venue for a reprex.

    Attributes:
        GH (str): GitHub-flavored Markdown
        DS (str): Discourse
        SO (str): StackOverflow
        HTML (str): HTML
        PY (str): Python script
        RTF (str): Rich Text Format
        SLACK (str): Slack markup
    """

    GH = "gh"
    DS = "ds"
    SO = "so"
    HTML = "html"
    PY = "py"
    RTF = "rtf"
    SLACK = "slack"


@dataclass
class ReprexConfig:
    """Configuration dataclass for reprexlite. Used to configure input parsing and output
    formatting.

    Args:
        editor (Optional[str]): Command-line program name of editor to use. If not specified,
            check $EDITOR and $VISUAL environment variables. If 'ipython', will launch the IPython
            interactive editor.
        venue (str): Key to identify the output venue that the reprex will be shared in. Used to
            select an appropriate formatter. See "Venues Formatting" documentation for formats
            included with reprexlite.
        advertise (bool): Whether to include a footer that credits reprexlite. If unspecified, will
            depend on specified venue formatter's default.
        session_info (bool): Include details about session and environment that the reprex was
            generated with.
        style (bool): Whether to autoformat code with black. Requires black to be installed.
        prompt (str): Prefix to use as primary prompt for code lines.
        continuation (str): Prefix to use as secondary prompt for continued code lines.
        comment (str): Prefix to use for results returned by expressions.
        keep_old_results (bool): Whether to additionally include results of expressions detected in
            the original input when formatting the reprex output.
        parsing_method (str): Method for parsing input. 'auto' will automatically detect either
            default reprex-style input or standard doctest-style input. 'declared' will allow you
            to specify custom line prefixes. Values for 'prompt', 'continuation', and 'comment'
            will be used for both output formatting and input parsing, unless the associated
            'input_*' override settings are supplied.
        input_prompt (str): Prefix to use as primary prompt for code lines when parsing input. Only
            used if 'parsing_method' is 'declared'. If not set, 'prompt' is used for both input
            parsing and output formatting.
        input_continuation (str): Prefix to use as secondary prompt for continued code lines when
            parsing input. Only used if 'parsing_method' is 'declared'. If not set, 'prompt' is
            used for both input parsing and output formatting.
        input_comment (str): Prefix to use for results returned by expressions when parsing input.
            Only used if 'parsing_method' is 'declared'. If not set, 'prompt' is used for both
            input parsing and output formatting.
    """

    editor: Annotated[Optional[str], Parameter(name=("--editor", "-e"))] = None
    # Formatting
    venue: Annotated[Venue, Parameter(name=("--venue", "-v"))] = Venue.GH
    advertise: Optional[bool] = None
    session_info: bool = False
    style: bool = False
    prompt: str = ""
    continuation: str = ""
    comment: str = "#>"
    keep_old_results: bool = False
    # Parsing
    parsing_method: ParsingMethod = ParsingMethod.AUTO
    input_prompt: Optional[str] = None
    input_continuation: Optional[str] = None
    input_comment: Optional[str] = None

    def __post_init__(self):
        # Validate venue
        try:
            Venue(self.venue)
        except ValueError:
            raise InvalidVenueError(
                f"{self.venue} is not a valid value for parsing method."
                f"Valid values are: {list(m.value for m in Venue)}"
            )
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
            raise InvalidParsingMethodError(
                f"{self.parsing_method} is not a valid value for parsing method."
                f"Valid values are: {[pm.value for pm in ParsingMethod]}"
            )

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
