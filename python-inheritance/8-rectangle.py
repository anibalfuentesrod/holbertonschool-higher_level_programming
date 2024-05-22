#!/usr/bin/python3
"""
A claass that inherit
"""


class BaseGeometry:
    """
    Class name
    """

    def area(self):
        """
        Raises an exception
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Args:
            name
            value

        Raises:
            TypeError
            ValueError
        """

        if type(value) is not int:
            raise TypeError(name + ' must be an integer')

        if value <= 0:
            raise ValueError(name + ' must be greater than 0')


"""
The class tha inherited
"""


class Rectangle(BaseGeometry):
    """
    defining the func name
    and add some privete to width and height
    """
    def __init__(self, width, height):
        """
        using the int validator on width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        """adding a comment here to intranet"""
        self.__width = width
        self.__height = height
