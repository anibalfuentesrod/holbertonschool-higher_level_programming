#!/usr/bin/python3
"""
This module has a func that adds two int
Prototype:
    def add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
    add two int or floats, casting floats to int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
