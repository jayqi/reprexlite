
clean: clean-build

clean-build:
	find . -name *.pyc -delete && find . -name __pycache__ -delete
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

build: clean-build
	python setup.py sdist bdist_wheel

lint:
	black --check reprexlite tests
	flake8 reprexlite tests

test:
	pytest -vv
