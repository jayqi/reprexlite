# reprexlite: Python reproducible examples for sharing

[![tests](https://github.com/jayqi/reprexlite/workflows/tests/badge.svg?branch=main)](https://github.com/jayqi/reprexlite/actions?query=workflow%3Atests+branch%3Amain)
[![codecov](https://codecov.io/gh/jayqi/reprexlite/branch/main/graph/badge.svg)](https://codecov.io/gh/jayqi/reprexlite)

**reprexlite** is tool for rendering **repr**oducible **ex**amples of Python code for sharing. It will execute your code and embed the results as comments below their associated lines. It is a lightweight alternative to [reprexpy](https://github.com/crew102/reprexpy) and is similarly meant as a port of the R package [reprex](https://github.com/tidyverse/reprex).

<a href="https://asciinema.org/a/391063" target="_blank"><img src="https://asciinema.org/a/391063.svg" width="480"/></a>

## Installation

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

This will take you into your system's default command-line text editor where you can type or paste your Python code. On macOS for example, this will be `vi`. You can set your default editor using the `$EDITOR` environment variable—I'm personally a fan of `nano`.

Once you're done, reprexlite will print out your reprex to console.

### Python library

```python
from reprexlite import reprex

code = """
arr = [1, 2, 3, 4, 5]
[x + 1 for x in arr]
"""

print(reprex(code))
```

## Comparison to reprexpy

Compared to reprexpy, reprexlite adds:

- A command-line interface so you can create reprexes without entering Python
- Lighter dependencies (e.g., no dependence on IPython)

However, reprexlite does not have:

- Direct ability to read from or write to your OS clipboard.
  - Instead, the CLI opens your default text editor which you can paste into.
- Automatic upload of matplotlib plots to imgur.com.
