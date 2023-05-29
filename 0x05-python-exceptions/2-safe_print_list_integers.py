#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i], end=""))
            printed_count + 1
    except (TypeError, ValueError):
        pass

        print()
        return printed_count
