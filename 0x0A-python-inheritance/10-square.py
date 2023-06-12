#!/usr/bin/python3
"""
Contains definition of class square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Implementing the class square which:
    inherits from the class Rectangle a subclass of class BaseGeometry
    """
    def __init__(self, size):
        """
        Instantiation of the square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Return area of a square
        """
        return self.__size ** 2
