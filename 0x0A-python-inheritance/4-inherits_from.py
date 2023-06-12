#!/usr/bin/python3
"""
Module implementation
"""


def inherits_from(obj, a_class):
    """
    Checking whether obj is a subclass of a_class
    Returns True if it is, otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
