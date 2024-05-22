#!/usr/bin/python3
"""
Makes sure the the value is int
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
