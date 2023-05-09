#!/usr/bin/python3

for j in range(ord('z'), ord('A') - 1, -1):
    print(f"{chr(j)}" if j % 2 == 0 else f"{chr(j - 32)}", end="")
