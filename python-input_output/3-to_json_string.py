#!/usr/bin/python3
"""
Writing a function that returns the JSON representation of an obj
"""
import json


def to_json_string(my_obj):
    """Using json.dumps, to meet the expectations"""
    return json.dumps(my_obj)
