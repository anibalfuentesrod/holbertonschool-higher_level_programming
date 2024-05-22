#!/usr/bin/python3
"""
Writing a func that returs true if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    my func returns the type() of obj and compares it to a_class
    Args:
        obj
        a_class
    """
    return type(obj) is a_class
