#!/usr/bin/python3
"""

This module defines a class Square....

"""


class Square:
    """

    A class to represent asquare

    This class has a private instance att size, with a getter and setter
    for validating its value. It also includes methods to calculate
    the area and print the square.

    """

    def __init__(self, size=0):
        """

        Initialize the square with an optional size att

        Args:
            size: The size of the square (defsult is 0)

        Raises:
            TypeErro: If size is not a int
            ValueError: If size is negative

        """
        self.size = size

    @property
    def size(self):
        """

        Getter for the size att

        Returns:
            The size of the square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """

        Setter for the size att

        Args:
            Value: The new size value

        Raise:
            TypeError: If size is not an inte
            ValueError: If size is negative

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """

        Calculate and returns the area of the square

        Returns:
            The area of the sqaure

        """
        return self.__size ** 2

    def my_print(self):
        """

        Print the size with the character #

        If size is 0, print an empty line

        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
