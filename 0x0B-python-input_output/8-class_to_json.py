#!/usr/bin/python3
"""
class-to_json function implementation
"""


def class_to_json(obj):
    """
    Returns a dictionary representation of a python object (list, bool,
    str, int, dictionary) for json serialization
    """
    return obj.__dict__
