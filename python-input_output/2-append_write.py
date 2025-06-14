#!/usr/bin/python3
"""Module that provides a function to append text to a file."""

def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 file and returns char count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
