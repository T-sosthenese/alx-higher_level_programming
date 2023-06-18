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

    def update(self, *args, **kwargs):
        """
        updates class square where:
        *args are the non-keyworded arguments
        **kwargs are the keyworded args
        **kwargs is skipped if args exists and is non-empty
        """
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Returns the dictionary representation of class square.
        """
        s_dict = {}
        s_dict["id"] = self.id
        s_dict["size"] = self.size
        s_dict["x"] = self.x
        s_dict["y"] = self.y
        return s_dict
