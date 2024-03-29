.PHONY: clean clean-dist docs format lint test typecheck

clean: clean-dist

clean-dist:
	find . -name *.pyc -delete && find . -name __pycache__ -delete
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

demo-render:
	terminalizer render docs/demo.yml -o docs/docs/images/demo.gif -q 100

docs:
	echo "# CLI Help Documentation\n" > docs/docs/cli.md
	@echo '```bash' >> docs/docs/cli.md
	@echo "reprex --help" >> docs/docs/cli.md
	@echo '```' >> docs/docs/cli.md
	@echo "" >> docs/docs/cli.md
	@echo '```' >> docs/docs/cli.md
	@reprex --help >> docs/docs/cli.md
	@echo '```' >> docs/docs/cli.md
	sed 's|https://raw.githubusercontent.com/jayqi/reprexlite/main/docs/docs/images/demo.gif|images/demo.gif|g' README.md \
		| sed 's|https://jayqi.github.io/reprexlite/stable/||g' \
		> docs/docs/index.md
	sed 's|https://jayqi.github.io/reprexlite/stable/||g' CHANGELOG.md \
		> docs/docs/changelog.md
	cd docs && mkdocs build


dist: clean-dist
	python -m build

format:
	ruff reprexlite tests --fix
	black reprexlite tests

generate-test-assets:
	python tests/expected_reprexes.py

lint:
	black --check reprexlite tests
	ruff reprexlite tests

test:
	pytest -vv

typecheck:
	mypy reprexlite --show-error-codes --install-types --non-interactive
