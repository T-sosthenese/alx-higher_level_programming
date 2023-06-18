#!/usr/bin/python3
"""
Class Rectangle documentation.
The class inherits from class Base.
Called using super id call.
"""

from models.base import Base


class Rectangle(Base):
    """
    This class inherits from the base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The class constructor.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width to the required value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """ x coordinate getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the x coordinate to a required value."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y coordinate getter."""
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the value of y equal to value."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculates the area of our rectangle using width and height
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle using '#' symbols
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """
        Overrides the __str__ method to print an informal
        representation of the string as specified.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        updates attributes in a list of *args
        where *args represents arbitary non-keyworded arguments
        and **kwargs is a dictionary of keyworded arguments
        """
        if len(args):
            for i, a in enumerate (args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle
        """
        r_dict = {}
        r_dict["id"] = self.id
        r_dict["width"] = self.width
        r_dict["height"] = self.height
        r_dict["x"] = self.x
        r_dict["y"] = self.y
        return r_dict
