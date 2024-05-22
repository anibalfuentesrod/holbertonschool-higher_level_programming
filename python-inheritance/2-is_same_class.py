#!/usr/bin/python3
"""
Writing a func that returs true if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    my func returns the type() of obj adn compares it to a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
