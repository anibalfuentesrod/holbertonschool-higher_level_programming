#!/usr/bin/python3
"""

This module defines a Square class with a private size attribute and
gette/setter

"""


class Square:
    """

    A class to respresent a square.

    This class has a private instance attribute size, with a getter and
    setter for validation its value

    """

    def __init__(self, size=0):
        """

        Initialize the Square with an optiona size attribute.

        Args:
            size: The size of the square (default is 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is negative
        """
        self.__size = size

    @property
    def size(self):
        """

        Getter for the size attribute

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """

        Setter for the size attribute

        Args:
            value: The new size value

        Raises:
            TypeError: If size is not an int
            ValueErro: IF size is negative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """

        Calculate and return the area of the square

        Return:
            The area of the square
        """
        return self.__size ** 2
