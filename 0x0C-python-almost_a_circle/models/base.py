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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves a json list of objects to a file.
        """
        filename = cls.__name__ + ".json"
        list_objects = []
        if list_objs is not None:
            for i in list_objs:
                list_objects.append(cls.to_dictionary(i))
        with open(filename, 'w', encoding='utf-8') as my_file:
            my_file.write(cls.to_json_string(list_objects))

    @staticmethod
    def from_json_string(json_string):
        """
        converts json string into list.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes set.
        """
        if cls.__name__ == "Rectangle":
            newbase = cls(1, 1)
        elif cls.__name__ == "Square":
            newbase = cls(1)
        newbase.update(**dictionary)
        return newbase
