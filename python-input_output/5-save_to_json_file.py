#!/usr/bin/python3
"""Writing a function that writes an Object to a text file, using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Using the built-in function dump()"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(my_obj, f)
    except PermissionError as pe:
        print(f"[PermissionEroor] {pe}")
    except TypeError as te:
        print(f"[TypeErronr] {te}")
