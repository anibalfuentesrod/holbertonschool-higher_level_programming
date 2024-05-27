#!/usr/bin/python3
"""
Writing a function that reads a txt file
"""


def read_file(filename=""):
    """This function takes a filename and i opened with the func open()
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
