#!/usr/bin/python3
"""Defines a rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a square."""

    def __init__(self, size):
        """initialize a new square.

        Args:
            size(int)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
