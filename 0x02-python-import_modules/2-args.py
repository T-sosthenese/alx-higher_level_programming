#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argc = len(sys.argv) - 1
    if argc == 0:
        print("{} arguments.".format(argc))
    else:
        if argc == 1:
            print("{} argument:".format(argc))
        else:
            print("{} arguments:".format(argc))
        for j in range(1, argc + 1):
            print("{}: {}".format(j, sys.argv[j]))
