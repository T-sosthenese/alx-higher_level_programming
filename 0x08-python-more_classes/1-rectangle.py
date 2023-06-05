#!/usr/bin/python3
"""
Module documentation
"""


class Rectangle:
    """
    An attempt to represent a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializing attributes to describe a rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retriving private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting private instance attribute width to a specified value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieving private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """An attempt to set the height of a rectangle to a preset value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
