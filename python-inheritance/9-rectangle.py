#!/usr/bin/python3
"""Rectangle class with area and string representation"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize and validate rectangle dimensions"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
