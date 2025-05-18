#!/usr/bin/python3
"""
This module provides a function to add two integers.

It includes type checking and conversion from float to int.
"""

def add_integer(a, b=98):
    """Add two integers or floats casted to integers.

    Args:
        a: first number (int or float)
        b: second number (int or float), default is 98

    Returns:
        The sum of a and b as an integer

    Raises:
        TypeError: if a or b are not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
