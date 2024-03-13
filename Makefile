install:
	poetry install

reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

test:
	poetry run pytest

lint:
	poetry run flake8 area

selfcheck:
	poetry check

build:
	poetry build

.PHONY: install test lint selfcheck check build