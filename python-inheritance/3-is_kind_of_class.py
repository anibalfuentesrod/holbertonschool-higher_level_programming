#!/usr/bin/python3
"""
Writing a func that returns true if the obj is an instance
of or if the obj is an instace of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance...

    Args:
        obj
        a_class
    Returns:
        True if obj is an instance of inherited from a class
    """
    return isinstance(obj, a_class)
