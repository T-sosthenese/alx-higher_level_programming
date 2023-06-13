#!/usr/bin/python3
""" pascal_triangle function documentation."""


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the Pascal's
    triangle."""

    if n <= 0:
        return ""
    p_triangle = [[1]]
    for current_row in range(1, n):
        row = [1]
        prev_row = p_triangle[current_row - 1]
        for element in range(1, current_row):
            row.append(pre_row[element] + prev_row[element - 1])
        row.append(1)
        p_triangle.append(row)
        return p_triangle
