#!/usr/bin/python3
"""
This function writes a string to .txt file
"""


def write_file(filename="", text=""):
    """
    In this function i make a code that return the number of char
    it has
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
