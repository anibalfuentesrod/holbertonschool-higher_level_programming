#!/usr/bin/python3
"""Creating module BaseGeometry."""


class BaseGeometry:
    """New BaseGeometry class."""
    def area(self):
        """The method to raise an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Code to take the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
