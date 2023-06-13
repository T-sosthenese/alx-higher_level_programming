#!/usr/bin/python3
"""
save_to_json_file module implementation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation
    """
    with open(filename, "w", encoding='utf-8') as my_file:
        object_json = json.dumps(my_obj)
        my_file.write(object_json)
