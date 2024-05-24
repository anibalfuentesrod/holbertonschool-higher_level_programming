#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


"""
making a class Shape with two subclasses name Circle, Rectangle
"""


class Shape(ABC):
    """
    Abstract base class represents a geometry shape

    Methods:
        area()
        perimeter()
    """
    @abstractmethod
    def area(self):
        """
        Calculates the area of the shape

        Returns:
            float: the area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates the perimeter of the shape

        Returns:
            float: the perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Circle class, subclass of Shape

    Parameters
        radius: float

    Methods:
        area()
        perimeter()
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    New class Rectangle, a subclass of Shape

    Parameters:
        width
        height
    Methods:
        area()
        perimeter()
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """
    Prints the area and perimeter of the given shape
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
