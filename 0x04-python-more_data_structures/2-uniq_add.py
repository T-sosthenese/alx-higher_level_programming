#!/usr/bin/python3

def uniq_add(my_list=[]):
    summation = 0
    for num in my_list:
        summation = sum(set(my_list))
    return summation
