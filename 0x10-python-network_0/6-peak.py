#!/usr/bin/python3
# Finding the peak of an array


def find_peak(list_of_integers):
    """Finds the highest number in a list of integers."""
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)
    else:
        length = len(list_of_integers)
        mid = int(length / 2)
        big = list_of_integers[mid]
        if big > list_of_integers[mid - 1] and big > list_of_integers[mid + 1]:
            return big
        elif big < list_of_integers[mid - 1]:
            return find_peak(list_of_integers[:mid])
        else:
            return find_peak(list_of_integers[mid + 1:])
