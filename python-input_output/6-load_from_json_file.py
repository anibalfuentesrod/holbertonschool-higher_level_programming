#!/usr/bin/python3
"""Writing a function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Using the built-in function load()"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("[FileNotFoundError] No such file or directory: '{}'".format(filename))
    except PermissionError:
        print("[PermissionError] Permission denied: '{}'".format(filename))
    except json.JSONDecodeError as e:
        print("[JSONDecodeError] {}".format(e))
