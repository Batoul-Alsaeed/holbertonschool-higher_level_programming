#!/usr/bin/python3
"""Defines a class Square with private size."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize the square with a private size.

        Args:
            size: The size of the square (no validation required yet)
        """
        self.__size = size
