# reprexlite: Python reproducible examples for sharing

[![PyPI](https://img.shields.io/pypi/v/reprexlite.svg)](https://pypi.org/project/reprexlite/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/reprexlite)](https://pypi.org/project/reprexlite/)
[![tests](https://github.com/jayqi/reprexlite/workflows/tests/badge.svg?branch=main)](https://github.com/jayqi/reprexlite/actions?query=workflow%3Atests+branch%3Amain)
[![codecov](https://codecov.io/gh/jayqi/reprexlite/branch/main/graph/badge.svg)](https://codecov.io/gh/jayqi/reprexlite)

**reprexlite** is tool for rendering **repr**oducible **ex**amples of Python code for sharing. It will execute your code and embed the outputs as comments below their associated lines. The rendered reprex can then be easily copied, pasted, and run as-is by anybody else. It is a lightweight alternative to [reprexpy](https://github.com/crew102/reprexpy) and is similarly meant as a port of the R package [reprex](https://github.com/tidyverse/reprex).

Here's an example of output created by reprexlite:

```python
arr = [1, 2, 3, 4, 5]
[x + 1 for x in arr]
#> [2, 3, 4, 5, 6]
```

<a href="https://asciinema.org/a/391063" target="_blank"><img src="https://asciinema.org/a/391063.svg" width="480"/></a>

#### Why reproducible examples?

If you're asking for help or reporting a bug, you are more likely to succeed in getting others to help you if you include a good reprex. If you're writing documentation, your readers will appreciate examples that they can easily run.

#### Why reprexlite?

reprexlite helps you create a self-contained reprex that can be easily copy-pasted and run. Your code runs in an isolated namespace. The reprex is formatted so that it is valid Python code with outputs as comments, unlike copying from a REPL. reprexlite is also very lightweight and has a convenient CLI, so you can easily and quickly get it up and running in a virtual environment.

## Installation

reprexlite is available on PyPI:

```bash
pip install reprexlite
```

Optional dependencies can be specified using the ["extras" mechanism](https://packaging.python.org/tutorials/installing-packages/#installing-setuptools-extras), e.g., `reprexlite[pygments]`. Available extras are:

- `black` : for optionally autoformatting your code
- `pygments` : for syntax highlighting and the RTF venue

### Development version

The development version of reprexlite is available on GitHub:

```bash
pip install https://github.com/jayqi/reprexlite.git#egg=reprexlite
```

## Quick usage

### Command-line interface

The reprexlite CLI allows you to create a reprex without entering Python. Simply invoke the command

```bash
reprex
```

This will take you into your system's default command-line text editor where you can type or paste your Python code. On macOS, for example, this will be `vi`. You can set your default editor using the `$EDITOR` environment variable—I'm personally a fan of `nano`.

Once you're done, reprexlite will print out your reprex to console.

### Python library

The same functionality as the CLI is also available from the `reprex` function with an equivalent API:

```python
from reprexlite import reprex

code = """
arr = [1, 2, 3, 4, 5]
[x + 1 for x in arr]
"""

reprex(code)
#> <reprexlite.reprex.GitHubReprex object at 0x7fd4446f94f0>
```

Under the hood, reprexlite is designed with a modular object-oriented architecture. See the [API documentation](https://jayqi.github.io/reprexlite/api-reference/reprex/) to learn more.

## Comparison to reprexpy

Compared to reprexpy, reprexlite adds:

- A command-line interface so you can create reprexes without entering Python
- Lighter dependencies (e.g., no dependence on IPython)

However, reprexlite does not have:

- Direct ability to read from or write to your OS clipboard.
  - Instead, the CLI opens your default text editor which you can paste into.
- Automatic upload of matplotlib plots to imgur.com.
