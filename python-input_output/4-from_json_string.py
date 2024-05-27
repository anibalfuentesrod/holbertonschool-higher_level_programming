#!/usr/bin/python3
"""Writing a function that return an obj represented by JSON"""
import json


def from_json_string(my_str):
    """Using built-in function loads()"""
    return json.loads(my_str)
