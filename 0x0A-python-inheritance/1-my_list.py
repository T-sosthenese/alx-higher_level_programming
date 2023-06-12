#!/usr/bin/python3
"""
Module documentation
"""


class MyList(list):
    def print_sorted(self):
        """
       Prints elements of a list in ascending order
       """
        sorted_list = sorted(self)
        print(sorted_list)
