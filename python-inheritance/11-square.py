#!/usr/bin/python3
"""Defines a rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""
    def __init__(self, size):
        """Initialize the Square with size."""
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
