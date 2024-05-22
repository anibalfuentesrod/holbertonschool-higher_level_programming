#!/usr/bin/python3
"""
Writing a func that returns true if the obj is an instance of a class
that inherited directly or indirectly
"""


def inherits_from(obj, a_class):
    """
    Checks if is inherited derectly or indirectly

    Parameters:
        obj
        a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
