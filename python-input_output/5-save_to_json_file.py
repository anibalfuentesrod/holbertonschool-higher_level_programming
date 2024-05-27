#!/usr/bin/python3
"""Writing a function that writes an Object to a text file, using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Using the built-in function dump()"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
