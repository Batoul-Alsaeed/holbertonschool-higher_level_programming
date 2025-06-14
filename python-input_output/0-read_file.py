#!/usr/bin/python3
"""Module that provides a function to read and print the
contents of a file."""


def read_file(filename=""):
    """Reads a UTF8 text file and prints its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
