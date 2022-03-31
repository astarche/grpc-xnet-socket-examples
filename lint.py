"""Lint the client."""
from os import system

system(rf"poetry run mypy client --check-untyped-defs")

system(rf"poetry run ni-python-styleguide lint client")
