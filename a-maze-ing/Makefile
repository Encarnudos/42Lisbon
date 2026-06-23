PYTHON ?= python3
CONFIG ?= config.txt


help:
	@echo "A-Maze-ing - available targets:"
	@echo "  make install      Install dev tools (flake8, mypy, build)"
	@echo "  make run          Run the program on \$$(CONFIG) [=$(CONFIG)]"
	@echo "  make debug        Run the program under pdb"
	@echo "  make lint         flake8 + mypy with the project flags"
	@echo "  make lint-strict  flake8 + mypy --strict"
	@echo "  make build        Build the mazegen package (sdist + wheel)"
	@echo "  make test         Run the unit tests with pytest"
	@echo "  make clean        Remove caches and build artifacts"

install:
	$(PYTHON) -m pip install --upgrade flake8 mypy build

run:
	$(PYTHON) a_maze_ing.py $(CONFIG)

debug:
	$(PYTHON) -m pdb a_maze_ing.py $(CONFIG)

lint:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --warn-return-any --warn-unused-ignores \
		--ignore-missing-imports --disallow-untyped-defs \
		--check-untyped-defs

lint-strict:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --strict

build:
	$(PYTHON) -m build

test:
	$(PYTHON) -m pytest -q

clean:
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
	rm -rf .mypy_cache .pytest_cache build dist *.egg-info

.PHONY: help install run debug lint lint-strict build test clean
