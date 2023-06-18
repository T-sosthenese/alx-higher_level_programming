#!/usr/bin/python3
"""
class Square documentation
This class inherits from class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square which inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiation of the class.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        Getter for square size.
        Returns size of the width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets the size of square sides equal to size.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overrides built-in __str__ to print a string in a specified format
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)
