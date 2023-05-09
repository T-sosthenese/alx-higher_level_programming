#!/usr/bin/python3

for j in range(0, 10):
    for k in range(j + 1, 10):
        print("{:d}{:d}".format(j, k), end="")
        if j == 8 and k == 9:
            print("")
        else:
            print(", ", end="")
