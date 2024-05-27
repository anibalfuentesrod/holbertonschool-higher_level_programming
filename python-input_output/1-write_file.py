#!/usr/bin/python3
"""
This function writes a string to .txt file
"""


def write_file(filename="", text=""):
    """

    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
