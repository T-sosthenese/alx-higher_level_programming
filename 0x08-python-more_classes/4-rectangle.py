#!/usr/bin/python3
"""
Module documentation
"""


class Rectangle:
    """Attempting to model a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing the attributes to describe our rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieving the private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Assigning the width to a specific value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieving the private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting private attribute height to a preset value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns the area of our rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method to return perimeter of our rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Printing the rectangle using # notation."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Returning a string representation of a rectangle."""
        new_rectangle = "Rectangle ({}, {})".format(self.__width, self.__height)
        return str(new_rectangle)
