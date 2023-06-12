#!/usr/bin/python3
"""
module implementation
"""


class BaseGeometry:
    """
    The class
    """
    def area(self):
        """
        Finding the area for class BaseGeometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates whether a given value is an integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
