#!/usr/bin/python3
"""
module for converting strings into json.
"""

import json


def from_json_string(my_str):
    """
    Convert from JSON string to a python data structure.
    """
    return json.loads(my_str)
