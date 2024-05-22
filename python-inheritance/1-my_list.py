#!/usr/bin/python3
"""
Writing a class that inherits list
"""


class MyList(list):
    """def a func that prints elements"""
    def print_sorted(self):
        print(sorted(self))
