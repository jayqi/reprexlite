"""This module holds metadata about formatted test cases. It also can be run as a script to
generate expected formatted test assets.

    python -m tests.expected_formatted
"""

from dataclasses import dataclass
from itertools import chain
from pathlib import Path
import shutil
from textwrap import dedent
from typing import Any, Dict

from reprexlite import reprex
from tests.utils import patch_datetime, patch_session_info, patch_version

ASSETS_DIR = (Path(__file__).parent / "assets" / "formatted").resolve()


INPUT = dedent(
    """\
    x = 2
    x + 2
    """
)


@dataclass
class ExpectedReprex:
    filename: str
    kwargs: Dict[str, Any]


expected_reprexes = [
    # Defaults
    ExpectedReprex("gh.md", {"venue": "gh"}),
    ExpectedReprex("so.md", {"venue": "so"}),
    ExpectedReprex("ds.md", {"venue": "ds"}),
    ExpectedReprex("htmlnocolor.html", {"venue": "htmlnocolor"}),
    ExpectedReprex("py.py", {"venue": "py"}),
    ExpectedReprex("slack.txt", {"venue": "slack"}),
    # With ad
    ExpectedReprex("ad/gh.md", {"venue": "gh", "advertise": True}),
    ExpectedReprex("ad/so.md", {"venue": "so", "advertise": True}),
    ExpectedReprex("ad/ds.md", {"venue": "ds", "advertise": True}),
    ExpectedReprex("ad/htmlnocolor.html", {"venue": "htmlnocolor", "advertise": True}),
    ExpectedReprex("ad/py.py", {"venue": "py", "advertise": True}),
    ExpectedReprex("ad/slack.txt", {"venue": "slack", "advertise": True}),
    # No ad
    ExpectedReprex("no_ad/gh.md", {"venue": "gh", "advertise": False}),
    ExpectedReprex("no_ad/so.md", {"venue": "so", "advertise": False}),
    ExpectedReprex("no_ad/ds.md", {"venue": "ds", "advertise": False}),
    ExpectedReprex("no_ad/htmlnocolor.html", {"venue": "htmlnocolor", "advertise": False}),
    ExpectedReprex("no_ad/py.py", {"venue": "py", "advertise": False}),
    ExpectedReprex("no_ad/slack.txt", {"venue": "slack", "advertise": False}),
    # With session info
    ExpectedReprex("session_info/gh.md", {"venue": "gh", "session_info": True}),
    ExpectedReprex("session_info/so.md", {"venue": "so", "session_info": True}),
    ExpectedReprex("session_info/ds.md", {"venue": "ds", "session_info": True}),
    ExpectedReprex(
        "session_info/htmlnocolor.html",
        {"venue": "htmlnocolor", "session_info": True},
    ),
    ExpectedReprex("session_info/py.py", {"venue": "py", "session_info": True}),
    ExpectedReprex("session_info/slack.txt", {"venue": "slack", "session_info": True}),
]

expected_reprexes_requires_pygments = [
    ExpectedReprex("html.html", {"venue": "html"}),
    ExpectedReprex("rtf.rtf", {"venue": "rtf"}),
    # With ad
    ExpectedReprex("ad/html.html", {"venue": "html", "advertise": True}),
    ExpectedReprex("ad/rtf.rtf", {"venue": "rtf", "advertise": True}),
    # No ad
    ExpectedReprex("no_ad/html.html", {"venue": "html", "advertise": False}),
    ExpectedReprex("no_ad/rtf.rtf", {"venue": "rtf", "advertise": False}),
    # With session info
    ExpectedReprex("session_info/html.html", {"venue": "html", "session_info": True}),
    ExpectedReprex("session_info/rtf.rtf", {"venue": "rtf", "session_info": True}),
]


if __name__ == "__main__":
    from tqdm import tqdm

    shutil.rmtree(ASSETS_DIR, ignore_errors=True)
    with patch_datetime(), patch_version(), patch_session_info():
        for ereprex in tqdm(chain(expected_reprexes, expected_reprexes_requires_pygments)):
            outfile = ASSETS_DIR / ereprex.filename
            outfile.parent.mkdir(exist_ok=True)
            reprex(INPUT, outfile=outfile, **ereprex.kwargs, print_=False)
