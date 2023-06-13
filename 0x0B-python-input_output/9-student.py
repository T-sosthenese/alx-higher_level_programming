#!/usr/bin/python3
"""
Class student documentation
"""


class Student:
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation process
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dict representation of a student instance.
        """
        return self.__dict__
