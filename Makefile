.PHONY: clean clean-dist docs format lint test typecheck

clean: clean-dist

clean-dist:
	find . -name *.pyc -delete && find . -name __pycache__ -delete
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

docs:
	echo "# CLI Help Documentation\n" > docs/docs/cli.md
	@echo '```bash' >> docs/docs/cli.md
	@echo "reprex --help" >> docs/docs/cli.md
	@echo '```' >> docs/docs/cli.md
	@echo "" >> docs/docs/cli.md
	@echo '```' >> docs/docs/cli.md
	@reprex --help >> docs/docs/cli.md
	@echo '```' >> docs/docs/cli.md
	cp README.md docs/docs/index.md
	cp HISTORY.md docs/docs/changelog.md
	cd docs && mkdocs build


dist: clean-dist
	python setup.py sdist bdist_wheel

format:
	isort reprexlite tests
	black reprexlite tests

lint:
	isort --check-only reprexlite tests
	black --check reprexlite tests
	flake8 reprexlite tests

test:
	pytest -vv

typecheck:
	mypy reprexlite
