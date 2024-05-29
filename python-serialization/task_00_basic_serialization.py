#!/usr/bin/python3
"""Creates basic serialization module"""
import json


def serialize_and_save_to_file(data, filename):
    """This func is to serialize the dict = data, and save on filename"""
    with open(filename, 'w') as j_file:
        json.dump(data, j_file)


def load_and_deserialize(filename):
    """Loads the json data in filename and desirialize into a dict"""

    with open(filename, 'r') as j_file:
        data = json.load(j_file)
    return data
