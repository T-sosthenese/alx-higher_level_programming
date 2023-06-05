#!/usr/bin/python3
"""
Module documentation
"""


class Rectangle:
    """"An attempt to model a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing attributes that describe our rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method to retrieve private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set private attribute width to a specific value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method to retrieve private attribute instance height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set private instance attribute to a specified value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method to calculate area of a rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method to calculate perimeter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print a series of # to represent a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """print self."""
        return "<{} object at {}>".format(type(self).__name__, hex(id(self)))
