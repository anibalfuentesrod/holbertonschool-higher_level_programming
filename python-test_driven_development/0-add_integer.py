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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = conv_int(a)
    b = conv_int(b)
    return int(a) + int(b)

def conv_int(num):
    if isinstance(num, float):
        num = int(num)
    return num
