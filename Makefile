.PHONY: pysetup pytest mypy flake8 pylint bandit black

help:
	@echo "pysetup - installs all requirements, activate virtual env before running"

pythonlint: blacklint mypy pylint flake8 bandit

pysetup:
	@echo "** Running python setup..."
	@echo "** Installing dependencies..."
	@poetry install

precommit-hook-setup:
	@echo "** Installing pre-commit hooks..."
	@. ./.venv/bin/activate && pre-commit install

pytest:
	@echo "** Running python tests..."
	@cd app/ && pytest;

mypy:
	@echo "** Running mypy..."
	@mypy --config-file app/mypy.ini app/

flake8:
	@echo "** Running flake8..."
	@flake8 --config=app/.flake8 app/

pylint:
	@echo "** Running pylint..."
	@pylint --load-plugins pylint_django --django-settings-module=core.settings --init-hook "import sys; import os; sys.path.append(os.path.join(os.getcwd(), 'app'))" --rcfile app/.pylintrc app/

bandit:
	@echo "** Running bandit..."
	@bandit -x app/tests -r app/

black:
	@echo "** Running black..."
	@black app --target-version py39 --line-length 119

blacklint:
	@echo "** Running black..."
	@black app --target-version py39 --line-length 119 --check
