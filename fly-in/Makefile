PYTHON := python3
MAP ?= maps/easy/01_linear_path.txt

.PHONY: install run debug clean lint lint-strict help

help:
	@echo "Targets:"
	@echo "  make install           install the dev tools (flake8, mypy)"
	@echo "  make run MAP=<file>     run the simulation on a map file"
	@echo "  make debug MAP=<file>   run the simulation under pdb"
	@echo "  make lint               flake8 + mypy (required flags)"
	@echo "  make lint-strict        flake8 + mypy --strict"
	@echo "  make clean              remove caches (__pycache__, .mypy_cache)"

install:
	$(PYTHON) -m pip install flake8 mypy

run:
	$(PYTHON) main.py $(MAP)

debug:
	$(PYTHON) -m pdb main.py $(MAP)

lint:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --strict

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf .mypy_cache
