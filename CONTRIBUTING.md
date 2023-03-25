# Contributing to reprexlite

[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json)](https://github.com/charliermarsh/ruff)
[![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![types - mypy](https://img.shields.io/badge/types-mypy-blue.svg)](https://github.com/python/mypy)

## Report a bug or request a feature

Please file an issue in the [issue tracker](https://github.com/jayqi/reprexlite/issues).

## Standalone tests

To run tests in your current environment, you should install from source with the `tests` extra to additionally install test dependencies. Then, use pytest to run the tests.

```bash
# Install with test dependencies
pip install .[tests]
# Run tests
pytest tests.py
```

## Developers guide

This project uses [Hatch](https://github.com/pypa/hatch) as its project management tool. The default environment includes dependencies for linting as well as all extra dependencies.

### Linting

To run linting or typechecking from the default environment:

```bash
hatch run lint
hatch run typecheck
```

### Tests

To run tests on the full test matrix, use the Hatch command:

```bash
hatch run tests:run
```
