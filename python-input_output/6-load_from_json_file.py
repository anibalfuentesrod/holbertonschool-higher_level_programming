#!/usr/bin/python3
"""Writing a function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Using the built-in function load()"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
