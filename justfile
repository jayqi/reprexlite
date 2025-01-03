python := shell("cat .python-version")

# Print this help documentation
help:
  just --list

# Sync dev environment dependencies
sync:
    uv sync --all-extras

# Run linting
lint:
    black --check reprexlite tests
    ruff check reprexlite tests

# Run static typechecking
typecheck:
    mypy reprexlite --install-types --non-interactive

# Run the tests
test:
    uv run --python {{python}} --all-extras --group test --isolated python -I -m pytest

test-all:
    for python in 3.8 3.9 3.10 3.11 3.12 3.13; do \
        just python=$python test; \
    done

# Generate test assets
generate-test-assets:
    uv run --python {{python}} --all-extras --group test --isolated python tests/expected_formatted.py
