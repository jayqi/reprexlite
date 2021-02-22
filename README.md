# reprexlite: Python reproducible examples for sharing

[![PyPI](https://img.shields.io/pypi/v/reprexlite.svg)](https://pypi.org/project/reprexlite/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/reprexlite)](https://pypi.org/project/reprexlite/)
[![tests](https://github.com/jayqi/reprexlite/workflows/tests/badge.svg?branch=main)](https://github.com/jayqi/reprexlite/actions?query=workflow%3Atests+branch%3Amain)
[![codecov](https://codecov.io/gh/jayqi/reprexlite/branch/main/graph/badge.svg)](https://codecov.io/gh/jayqi/reprexlite)

**reprexlite** is tool for rendering **repr**oducible **ex**amples of Python code for sharing. It will execute your code and embed the outputs as comments below their associated lines. The rendered reprex can then be easily copied, pasted, and run as-is by anybody else. It is a lightweight alternative to [reprexpy](https://github.com/crew102/reprexpy) and is similarly meant as a port of the R package [reprex](https://github.com/tidyverse/reprex).

Here's an example of output created by reprexlite:

```python
from itertools import product

grid = list(product([1, 2, 3], [8, 16]))
grid
#> [(1, 8), (1, 16), (2, 8), (2, 16), (3, 8), (3, 16)]
list(zip(*grid))
#> [(1, 1, 2, 2, 3, 3), (8, 16, 8, 16, 8, 16)]
```

<a href="https://asciinema.org/a/391063" target="_blank"><img src="https://asciinema.org/a/391063.svg" width="480"/></a>

#### Why reproducible examples?

If you're asking for help or reporting a bug, you are more likely to succeed in getting others to help you if you include a good reprex. If you're writing documentation, your readers will appreciate examples that they can easily run.

#### Why reprexlite?

reprexlite helps you create a self-contained reprex that can be easily copied, paste, and run. Your code runs in an isolated namespace. The reprex is formatted so that it is valid Python code with outputs as comments, unlike copying from a REPL. reprexlite is also very lightweight and has a convenient CLI, so you can easily and quickly get it up and running in a virtual environment.

See ["Design Philosphy"](https://jayqi.github.io/reprexlite/design-philosophy/) for more on both "Why reproducible examples?" and "Why reprexlite?"

## Installation

reprexlite is available on PyPI:

```bash
pip install reprexlite
```

Optional dependencies can be specified using the ["extras" mechanism](https://packaging.python.org/tutorials/installing-packages/#installing-setuptools-extras), e.g., `reprexlite[black]`. Available extras are:

- `black` : for optionally autoformatting your code
- `pygments` : for syntax highlighting and the RTF venue

### Development version

The development version of reprexlite is available on GitHub:

```bash
pip install https://github.com/jayqi/reprexlite.git#egg=reprexlite
```

## Quick usage

### Command-line interface

The reprexlite CLI allows you to create a reprex without entering a Python session. Simply invoke the command:

```bash
reprex
```

This will take you into your system's default command-line text editor where you can type or paste your Python code. On macOS, for example, this will be `vim`. You can set your default editor using the `$EDITOR` environment variable—I'm personally a fan of `nano`.

Once you're done, reprexlite will print out your reprex to console.

To see available options, use the `--help` flag.

### Python library

The same functionality as the CLI is also available from the `reprex` function with an equivalent API. Simply pass a string with your code, and it will print out the reprex, as well as return a `Reprex` object that contains all the data and formatting machinery. See the [API documentation](https://jayqi.github.io/reprexlite/api-reference/reprex/) for more details.

```python
from reprexlite import reprex

code = """
from itertools import product

grid = list(product([1, 2, 3], [8, 16]))
grid
list(zip(*grid))
"""

reprex(code)
#> ```python
#> from itertools import product
#>
#> grid = list(product([1, 2, 3], [8, 16]))
#> grid
#> #> [(1, 8), (1, 16), (2, 8), (2, 16), (3, 8), (3, 16)]
#> list(zip(*grid))
#> #> [(1, 1, 2, 2, 3, 3), (8, 16, 8, 16, 8, 16)]
#> ```
#>
#> <sup>Created at 2021-02-21 10:27:37 PST by [reprexlite](https://github.com/jayqi/reprexlite) v0.2.0</sup>
#> <reprexlite.formatting.GitHubReprex object at 0x7ff7bd3111c0>
```
