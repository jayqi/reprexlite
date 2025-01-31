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

# Run tests
test *args:
    uv run --python {{python}} --no-editable --all-extras --no-dev --group test --isolated \
        python -I -m pytest -n auto {{args}}

test-no-dist *args:
    uv run --python {{python}} --no-editable --all-extras --no-dev --group test --isolated \
        python -I -m pytest -n0 --dist no {{args}}

# Run all tests with Python version matrix
test-all:
    for python in 3.8 3.9 3.10 3.11 3.12 3.13; do \
        just python=$python test; \
    done

# Generate test assets
generate-test-assets:
    uv run --python {{python}} --all-extras --no-dev --group test  --isolated \
        python -I tests/expected_formatted.py

# Generate docs website
docs:
    @echo "# CLI Help Documentation\n" > docs/docs/cli.md
    @echo '```bash' >> docs/docs/cli.md
    @echo "reprex --help" >> docs/docs/cli.md
    @echo '```' >> docs/docs/cli.md
    @echo "" >> docs/docs/cli.md
    @echo '```' >> docs/docs/cli.md
    @uv run reprex --help >> docs/docs/cli.md
    @echo '```' >> docs/docs/cli.md
    sed 's|https://raw.githubusercontent.com/jayqi/reprexlite/main/docs/docs/images/demo.gif|images/demo.gif|g' README.md \
        | sed 's|https://jayqi.github.io/reprexlite/stable/||g' \
        > docs/docs/index.md
    sed 's|https://jayqi.github.io/reprexlite/stable/||g' CHANGELOG.md \
        > docs/docs/changelog.md
    uv run --python {{python}} --no-dev --group docs --isolated \
        --directory docs/ \
        python -I -m mkdocs build

# Serve built docs
docs-serve:
    uv tool run quickhttp docs/site/
