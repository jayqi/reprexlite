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
	sed 's|https://jayqi.github.io/reprexlite/stable/||g' HISTORY.md \
		> docs/docs/changelog.md
	cd docs && mkdocs build


dist: clean-dist
	python setup.py sdist bdist_wheel

format:
	isort reprexlite tests
	black reprexlite tests

generate-test-assets:
	python tests/expected_reprexes.py

lint:
	isort --check-only reprexlite tests
	black --check reprexlite tests
	flake8 reprexlite tests

test:
	pytest -vv

typecheck:
	mypy reprexlite
