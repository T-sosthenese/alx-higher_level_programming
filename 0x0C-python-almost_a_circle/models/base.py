#!/usr/bin/python3
"""
Class base documentation.
"""

import json


class Base:
    """
    The base class for all classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Base class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the json string representation of a python dictionary.
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
