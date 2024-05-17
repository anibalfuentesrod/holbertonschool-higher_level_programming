#!/usr/bin/python3
"""

This module defines a Square class with a priv size and position att
and provides methods to get and set these att, calculate aream and
prints the square

"""


class Square:
    """

    A class to respresent a square.

    This class has a private instance att size and position, with
    getter and setter for validating their values. It also includes
    methods to calculate the area and prints the square too.

    """

    def __init__(self, size=0, position=(0, 0)):
        """

        Initialize the Square with optional size and position att

        Args:
            size: The size of the square (default is 0)
            position: A tuple of 2 positive int representing
            the position (default is (0, 0))

        Raises:
            TypeError: If size is not an int or positive is not a tuple
            of 2 positive int

            ValueErro: If size is less than 0 op positvie contains
            negative values

        """
        self.size = size  # Using the setter for validation
        self.position = position  # Using the seeter for val

    @property
    def size(self):
        """

        Getter for the size att

        Returns:
            THe size of the square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """

        Setter for the size att

        Args:
            value: The new size value

        Raises:
            TypeError: If size is not an int
            ValueError: If size is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """

        Getter for the position att

        Returns:
            The position of the square

        """
        return self.__position

    @position.setter
    def position(self, value):
        """

        Setter for the position value

        Args:
            value: The new position value

        Raises:
            TypeErro: If position is not a tuple of 2 positive int
            ValueError: If position contains negative values

        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) for num in value) and
                all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """

        Calculate and returns the are of the square

        Reuturns:
            The are of the square

        """
        return self.__size ** 2

    def my_print(self):
        """

        Prints the square with the character #

        If size is 0, print an empty line. THe position att is use
        to offset the square.

        """
        if self.__size == 0:
            print("")
            return
        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
