#!/usr/bin/python3
"""Defines a Square class that can print itself."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize square with size using the setter."""
        self.size = size

    @property
    def size(self):
        """Get current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
