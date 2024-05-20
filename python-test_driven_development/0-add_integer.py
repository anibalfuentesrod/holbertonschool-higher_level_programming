#!/usr/bin/python3
"""
This module has a func that adds two int
Prototype:
    def add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
    Function that adds two int
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
