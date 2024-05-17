#!/usr/bin/python3
"""

This module defines a class name Square with a private size attribute
The size attribute must be an integer and cannot be negative

"""


class Square:
    """

    A class that represents a square

    This class has a private instance attribute size, which must be
    an int and cannot be negative

    """
    def __init__(self, size=0):
        """

        Initialize the Square with an optional size atributte

        Args:
            size: The size of the square (default is 0).

        Raise:
            TypeError: If size is not an integer
            ValueError: If size is negative

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
        """

        Calculate and return the area of the square

        Returns:
            The are of the square

        """
        return self.__size ** 2
