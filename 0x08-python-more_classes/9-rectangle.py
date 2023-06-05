#!/usr/bin/python3
"""
Module documentation
"""


class Rectangle:
    """Attempting to model a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing the attributes to describe our rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        ms = "\n".join([str(self.print_symbol) * self.__width] * self.__height)
        return ms

    def __repr__(self):
        """Returning a string representation of a rectangle."""
        width = str(self.__width)
        height = str(self.__height)
        new_rectangle = "Rectangle(" + width + ", " + height + ")"
        return new_rectangle

    def __del__(self):
        """Prints good bye after deleting our rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new Rectangle instance with equal width and height."""
        return cls(size, size)
