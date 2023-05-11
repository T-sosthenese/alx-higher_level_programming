#!/usr/bin/python3
""" Module to perform basic calculations """
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    op = {'+': add, '-': sub, '*': mul, '/': div}
    argc = len(argv) - 1  # Calculating the number of arguments

    if argc != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])  # Defining variable a as second arg
    operator = argv[2]  # Operator comes immediately after first variable
    b = int(argv[3])  # Var b is the fourth argument

    if operator not in op.keys():
        print("Unknown operator. Available operators: +, -, * and /")

    result = op[operator](a, b)  # Performing all types of operations in loop
    print("{} {} {} = {}".format(a, operator, b, result))
