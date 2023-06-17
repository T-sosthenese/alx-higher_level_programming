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
        return __width

    @width.setter
    def width(self, value):
        """ sets the width to the required value."""
        self.__width = value

    @property
    def height(self):
        """height getter """
        return __height

    @height.setter
    def height(self, value):
        """ height setter """
        self.__height = value

    @property
    def x(self):
        """ x coordinate getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the x coordinate to a required value."""
        self.__x = value

    @property
    def y(self):
        """ y coordinate getter."""
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the value of y equal to value."""
        self.__y = value
