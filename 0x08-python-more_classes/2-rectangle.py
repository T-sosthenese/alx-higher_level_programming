#!/usr/bin/python3
"""
Module documentation
"""


class Rectangle:
    """An attempt to represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing attribues to describe a rectanle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method to retrieve private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting width to a specified value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A method to retrieve private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set height to a specified value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method to return the area of a rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """public instance method to return the perimeter of a rectangle."""
        return 2 * (self.__width + self.__height)
