#!/usr/bin/python3
"""Defines a Square class that supports comparisons."""


class Square:
    """Represents a square that can be compared by area."""

    def __init__(self, size=0):
        """Initialize square with validated size."""
        self.size = size

    @property
    def size(self):
        """Get current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with type and value validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    # Comparison operators based on area
    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
