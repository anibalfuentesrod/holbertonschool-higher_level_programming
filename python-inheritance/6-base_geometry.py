#!/usr/bin/python3
"""
Making a class that raises an error
"""


class BaseGeometry:
    """
    Raises:
        TypeError
    """
    def area(self):
        raise Exception("area() is not implemented")
