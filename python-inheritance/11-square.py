#!/usr/bin/python3
"""so yeahhh this nedd comments here"""
Rectangle = __import__('9-rectangle').Rectangle
"""
making a new inherited class call square
"""


class Square(Rectangle):
    """A class representing a square."""
    def __init__(self, size):
        """Initialize the Square with size."""
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
