#!/usr/bin/python3
"""
module implementation
"""


def write_file(filename="", text=""):
    """
    A function that writes a given string into a file.
    Returns the number of characters writen.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        characters_written = file.write(text)
    return characters_written
