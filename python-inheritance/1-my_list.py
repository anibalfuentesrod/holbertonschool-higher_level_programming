#!/usr/bin/python3
"""simple class"""


class MyList(list):
    """def a func that prints elements"""
    def print_sorted(self):
        print(sorted(self))
