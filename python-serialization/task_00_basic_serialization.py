#!/usr/bin/python3
"""Creates basic serialization module"""
import json


def serialize_and_save_to_file(data, filename):
    """This func is to serialize the dict = data, and save on filename"""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def load_and_deserialize(filename):
    """Loads the json data in filename and desirialize into a dict"""

    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data
