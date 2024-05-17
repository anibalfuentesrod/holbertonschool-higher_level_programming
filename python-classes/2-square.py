#!/usr/bin/python3
"""

This module defines a Square class with a private size attribute
The size attribute must be an integer and cannot be negative

"""


class Square:
    """

    A class to represent a Square

    This class has a private instance attributte size, tha has to be
    an int, and cannot be negative

    """

    def __init__(self, size=0):
        """

        Initialize the Square with an optional size attribute.

        Args:
            size: The size of the square (default is 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is negative

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
