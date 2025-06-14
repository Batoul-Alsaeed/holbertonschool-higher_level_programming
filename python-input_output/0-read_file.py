#!/usr/bin/python3
def read_file(filename=""):
        """Reads a text file (UTF8) and prints its contents to stdout."""
    whit open(filename, "r", encoding="UTF8.txt") as f:
        print(f.read(), end="")
