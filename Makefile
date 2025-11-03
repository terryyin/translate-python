clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

lint:
	pre-commit run -av

# Check if Python version is 3.11+ for --break-system-packages flag
BREAK_FLAG := $(shell python3 -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)" 2>/dev/null && echo "--break-system-packages" || echo "")

pip-install:
	pip install --user $(BREAK_FLAG) -r requirements-dev.txt
pip-install-build:
	pip install --user $(BREAK_FLAG) -r requirements-build.txt

pip-upgrade:
	pip install --user --upgrade $(BREAK_FLAG) -r requirements-dev.txt

cov:
	coverage report -m
	codecov --token=485a9f45-2294-40d1-bc09-0675629d418f

cov-report:
	py.test -vv --cov-report=html tests

test: pip-install-build
	py.test -vv -s

build: test
	python setup.py sdist
	python setup.py bdist_wheel

release: build
	git tag `python setup.py -q version`
	git push origin `python setup.py -q version`
	twine upload dist/*
