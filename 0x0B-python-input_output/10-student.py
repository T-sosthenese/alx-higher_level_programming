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

        if not isinstance(attrs, list):
            return self.__dict__
        for attribute in attrs:
            if not isinstance(attribute, str):
                return self.__dict__
        new_dict = {}
        for str_att in attrs:
            if str_attr in self.__dict__.keys():
                new_dict[str_attr] = self.__dict__[str_att]
        return new_dict
