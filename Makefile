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

dev:
	pip install -r requirements-dev.txt

test: dev
	py.test -vv -s

build: test
	python setup.py sdist
	python setup.py bdist_wheel

${VIRTUAL_ENV}/bin/pip-sync:
	pip install pip-tools

pip-tools: ${VIRTUAL_ENV}/bin/pip-sync

pip-compile: pip-tools
	@rm -r requirements.txt
	pip-compile requirements.in

pip-install: pip-compile
	pip install --upgrade -r requirements-dev.txt

pip-upgrade: pip-tools
	pip-compile --upgrade requirements.in
