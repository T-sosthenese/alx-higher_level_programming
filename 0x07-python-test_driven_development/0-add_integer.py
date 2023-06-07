#!/usr/bin/python3
"""
0-add_integer module
"""


def add_integer(a, b=98):
    """
    Adds two numbers after confirming they are either int or float
    Casts floats into integers before returning the sum
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
