#!/usr/bin/python3
# Finding the peak of an array


def find_peak(list_of_integers):
    """Finds the highest number in a list of integers."""
    length = len(list_of_integers)

    left = 0 # leftmost index
    right = length - 1 # rightmost index

    if length == 0:
        return None

    while (left < right):
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
