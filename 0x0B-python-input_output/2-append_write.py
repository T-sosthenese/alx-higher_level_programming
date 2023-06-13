#!/usr/bin/python3
"""
module implementation for appending string to a file
"""


def append_write(filename="", text=""):
    """
    A function that appends text to a file.
    Creates a file if the file does not exist.
    Returns the number of characters appended.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        characters_added = file.write(text)
    return characters_added
