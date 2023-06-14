#!/usr/bin/python3
"""
Adding some text after specified string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after a specific string sequence.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, mode='w') as f:
        new_lines = []
        for i in range(len(lines)):
            new_lines.append(lines[i])
            if search_string in lines[i]:
                new_lines.append(new_string)
            f.writelines(new_lines)
