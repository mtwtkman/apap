.PHONY:

test:
	poetry run python -m unittest tests

type:
	poetry run mypy apap

lint:
	poetry run black apap/*.py tests/**/*.py tests/*.py

check:
	make lint && make type && make test && poetry install

pub:
	make check && poetry publish --build
