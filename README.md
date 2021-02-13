# reprexlite: Python reproducible examples for sharing

**reprexlite** is tool for rendering reproducible examples of Python code for sharing. It's a lightweight alternative to [reprexpy](https://github.com/crew102/reprexpy) and is similarly meant as a port of the R package [reprex](https://github.com/tidyverse/reprex).

## Installation

```bash
pip install https://github.com/jayqi/reprexlite.git#egg=reprexlite
```

## Comparison to reprexpy

Compared to reprexpy, reprexlite adds:

- A command-line interface so you can create reprexes without entering Python
- Much fewer dependencies (no dependence on IPython)

However, reprexlite does not have:

- Direct ability to read from or write to your OS clipboard.
  - Instead, the CLI opens your default text editor which you can paste into.
- Automatic upload of plots or other images to imgur.com.
