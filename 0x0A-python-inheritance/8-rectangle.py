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


class Rectangle(BaseGeometry):
    """
    The Rectangle class which inherits from class BaseGeometry
    Args:
        width
        height
    """
    def __init__(self, width, height):
        """
        Instantiation of the rectangle instance
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
