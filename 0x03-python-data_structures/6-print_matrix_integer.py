#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    for row in matrix:
        for i, item in enumerate(row):
            # If it is not the last item, add a spece after it
            if i != len(row) - 1:
                print("{:d}".format(item), end=" ")
            else:
                # If it is the last item, end the line
                print("{:d}".format(item))
