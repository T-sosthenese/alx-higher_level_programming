#!/usr/bin/python3
# Finding the peak of an array


def find_peak(list_of_integers):
    """Finds the highest number in a list of integers."""
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        k = len(list_of_integers)
        peak_integer = list_of_integers[0]
        for i in range(1, k):
            if list_of_integers[i] > peak_integer:
                peak_integer = list_of_integers[i]
        return peak_integer
