#!/usr/bin/python3
"""BaseGeometry module with area method that is not implemented"""


class BaseGeometry:
    """Base class for geometry operations"""

    def area(self):
        """Raises an Exception indicating area is not implemented"""
        raise Exception("area() is not implemented")
