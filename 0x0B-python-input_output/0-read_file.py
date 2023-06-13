#!/usr/bin/python3
"""
module implementation for file I/O in python
"""


def read_file(filename=""):
    """
    A function that reads a string from a file and prints it to the stdout.
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')
