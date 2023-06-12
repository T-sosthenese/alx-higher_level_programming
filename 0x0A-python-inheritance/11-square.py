#!/usr/bin/python3
"""
Contains implementation of class square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Implementation of class Square that inherits from class Rectangle.
    """
    def __init__(self, size):
        """
        Instantiation of class Square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Method for calculating the area of a square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns string representation of the square.
        """
        return "[{}] {}/{}".format(type(self).__name__, self.__size,
                                   self.__size)
