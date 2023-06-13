#!/usr/bin/python3
""" pascal_triangle function documentation."""


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the Pascal's
    triangle."""

    if n <= 0:
        return list()

    tr = []
    for line in range(0, n):
        tmp = []
        for i in range(0, line + 1):
            tmp.append(magic(line, i))
        tr.append(tmp)
    return tr


def magic(n, k):
    """
    does some magic
    """
    result = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        result = result * (n - i)
        result = result // (i + 1)
    return result
