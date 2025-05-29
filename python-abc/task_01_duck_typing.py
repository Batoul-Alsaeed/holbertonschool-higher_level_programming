#!/usr/bin/env python3
"""
Defines an abstract class 'Shape' and two subclasses 'Circle' and 'Rectangle'.
Includes a function 'shape_info' that prints area and perimeter using duck typing.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Abstract base class for shapes.
    """
    @abstractmethod
    def area(self):
        """Calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter"""
        pass

class Circle(Shape):
    """
    A circle shape with area and perimeter methods.
    Handles negative radius using abs().
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)

class Rectangle(Shape):
    """
    A rectangle shape with width and height.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Uses duck typing to print area and perimeter of any shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
