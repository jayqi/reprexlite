
clean: clean-dist

clean-dist:
	find . -name *.pyc -delete && find . -name __pycache__ -delete
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

dist: clean-dist
	python setup.py sdist bdist_wheel

lint:
	black --check reprexlite tests
	flake8 reprexlite tests

test:
	pytest -vv

typecheck:
	mypy reprexlite
