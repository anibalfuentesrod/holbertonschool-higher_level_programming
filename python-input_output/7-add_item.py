#!/usr/bin/python3
"""Writing a scrip that adds all arguments to a py list and then save it
"""
import sys


if __name__ == "__main__":
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file.py').load_from_json_file

    try:
        item = load_from_json("add_item.json")
    except FileNotFoundError:
        item = []
    item.extend(sys.argv[1:])
    save_to_json(item, "add_item.json")
