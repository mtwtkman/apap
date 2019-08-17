.PHONY:

test:
	poetry run python -m unittest tests

type:
	poetry run mypy apap

lint:
	poetry run black apap/*.py tests/**/*.py tests/*.py

rst:
	poetry run rst-lint README.rst

check: lint type test rst
	poetry install

pub:
	make check && poetry publish --build
