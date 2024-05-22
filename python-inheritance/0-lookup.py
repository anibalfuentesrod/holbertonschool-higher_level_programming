#!/usr/bin/python3
"""
Writing a func that returns the list of att and methods
of an object
"""


def lookup(obj):
    """
    making a new var that has a value of dir() so that i can return it
    """
    att_obj = dir(obj)
    return att_obj
