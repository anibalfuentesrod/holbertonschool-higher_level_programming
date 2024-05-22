#!/usr/bin/python3
"""
Making a class with methods for area and int validation
"""


class BaseGeometry:
    """Raises an exception indicating that area ins not implemented"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the value is positive

        Args:
            name
            value
        Raises:
            TypeError
            ValueError
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
