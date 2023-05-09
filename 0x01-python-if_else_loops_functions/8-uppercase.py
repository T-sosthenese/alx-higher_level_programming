#!/usr/bin/python3

def uppercase(str):
    for j in str:
        if ord(j) >= 97 and ord(j) <= 122:
            c = chr(ord(j) - 32)
        else:
            c = j
        print("{}".format(c), end="")
    print("")
