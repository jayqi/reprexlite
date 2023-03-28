"""This module holds metadata about formatted test cases. It also can be run as a script to
generate expected formatted test assets.

    python -m tests.expected_formatted
"""

from contextlib import redirect_stdout
from dataclasses import dataclass
from itertools import chain
from pathlib import Path
import shutil
from textwrap import dedent
from typing import Any, Dict

from reprexlite import reprex
from tests.utils import patch_datetime, patch_version

ASSETS_DIR = (Path(__file__).parent / "assets" / "printed").resolve()


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
    ExpectedReprex("html.html", {"venue": "html"}),
    ExpectedReprex("htmlnocolor.html", {"venue": "htmlnocolor"}),
    ExpectedReprex("py.py", {"venue": "py"}),
    ExpectedReprex("slack.txt", {"venue": "slack"}),
]
expected_reprexes_no_color = [
    # No Color
    ExpectedReprex("no_color/gh.md", {"venue": "gh", "no_color": True}),
    ExpectedReprex("no_color/so.md", {"venue": "so", "no_color": True}),
    ExpectedReprex("no_color/ds.md", {"venue": "ds", "no_color": True}),
    ExpectedReprex("no_color/html.html", {"venue": "html", "no_color": True}),
    ExpectedReprex("no_color/htmlnocolor.html", {"venue": "htmlnocolor", "no_color": True}),
    ExpectedReprex("no_color/py.py", {"venue": "py", "no_color": True}),
    ExpectedReprex("no_color/slack.txt", {"venue": "slack", "no_color": True}),
]

if __name__ == "__main__":
    import rich  # noqa: F401
    from tqdm import tqdm

    shutil.rmtree(ASSETS_DIR, ignore_errors=True)
    with patch_datetime(), patch_version():
        for ereprex in tqdm(
            list(
                chain(
                    expected_reprexes,
                    expected_reprexes_no_color,
                )
            )
        ):
            outfile = ASSETS_DIR / ereprex.filename
            outfile.parent.mkdir(exist_ok=True)
            r = reprex(INPUT, **ereprex.kwargs, print_=False)
            with outfile.open("w") as fp:
                with redirect_stdout(fp):
                    r.print()
