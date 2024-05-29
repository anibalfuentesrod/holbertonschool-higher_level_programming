#!/usr/bin/python3
"""Reading data on CSV formatand converts the format on JSON"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Function that converts CSV file to JSON"""
    try:
        with open(csv_filename, mode='r') as csv_f:
            csv_reader = csv.DictReader(csv_f)
            data = [row for row in csv_reader]

        with open('data.json', mode='w') as json_f:
            json.dump(data, json_f, indent=4)

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
