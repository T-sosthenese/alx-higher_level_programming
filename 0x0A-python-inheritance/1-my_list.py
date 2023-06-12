#!/usr/bin/python3
"""
Module documentation
"""


class MyList(list):
    """
    Inheriting the list class from python
    """
    def print_sorted(self):
        """
       Prints elements of a list in ascending order
       """
        print(sorted(set(self)))
