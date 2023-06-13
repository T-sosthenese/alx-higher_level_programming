#!/usr/bin/python3
"""
load_from_json_file module implementation
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    Returns JSON object represented by string in the file.
    """
    with open(filename, "r", encoding='utf-8') as my_file:
        return json.loads(my_file.read())
