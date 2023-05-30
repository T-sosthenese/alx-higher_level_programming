#!/usr/bin/python3
"""
module documentation
"""


class Square:
    """
    the class itself
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        returns the area based on the side dimensions
        """
        squared = self.__size ** 2
        return squared

    def my_print(self):
        if self.__size == 0:
            print()
            return None

        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
