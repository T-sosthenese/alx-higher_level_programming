#!/usr/bin/python3
""" Class student implementation."""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """Instantation of class student."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dictionary representation of a student instance."""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        """
        Replaces all sttributes in the student instance with thosse in
        json arguments.
        """
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
