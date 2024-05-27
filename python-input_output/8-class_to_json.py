#!/usr/bin/python3
"""Wrtiting a func that returns a dictionary descrition"""


def class_to_json(obj):
    """Returns a dictionary descritpion with simple date structure"""
    att = obj.__dict__
    json_dict = {}

    for key, value in att.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
