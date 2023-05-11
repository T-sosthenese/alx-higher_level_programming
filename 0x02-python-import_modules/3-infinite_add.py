#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv[1:]  # Excluding the first argument (filename)
    argument_summation = sum(int(arg) for arg in args)
    print(argument_summation)
