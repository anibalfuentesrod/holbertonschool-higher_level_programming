#!/usr/bin/python3
"""
Writing a functiona that appends to a file
"""


def append_write(filename="", text=""):
    """
    Giving the function the permission append = 'a'
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
