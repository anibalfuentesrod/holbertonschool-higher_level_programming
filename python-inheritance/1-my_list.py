#!/usr/bin/python3
"""
Writing a class "MyList" that inherits: list
"""


class MyList(list):
    """
    def a func that prints the list of elements in ascending
    sorted oreder
    """
    def print_sorted(self):
        print(sorted(self))