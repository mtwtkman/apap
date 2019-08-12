.PHONY:

test:
	poetry run python -m unittest discover -p test_*.py

type:
	poetry run mypy apap

lint:
	poetry run black apap/*.py tests/**/*.py tests/*.py

check:
	make lint && make type && make test

pub:
	make check && poetry publish --build
