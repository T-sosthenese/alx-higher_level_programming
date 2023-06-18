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
