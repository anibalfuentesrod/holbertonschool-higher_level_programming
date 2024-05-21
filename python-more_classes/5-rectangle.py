#!/usr/bin/python3
"""
This class define a rectangle
"""


class Rectangle:
    """
    Define some func, like: height, width, area, perimiter.

    Raises:
        TypeError
        ValueError
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimiter of the reactangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a str representation if the rec... with char #"""
        if self.__width == 0 or self.height == 0:
            return ""

        rectangle_rows = []
        for _ in range(self.__height):
            rectangle_rows.append("#" * self.__width)

        rectangle_str = "\n".join(rectangle_rows)
        return rectangle_str

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance is deleted"""
        print("Bye rectangle...")
