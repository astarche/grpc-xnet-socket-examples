"""Lint the client."""
from subprocess import run

run(rf"mypy client --check-untyped-defs", shell=True, check=True)

run(rf"ni-python-styleguide lint client", shell=True, check=True)
