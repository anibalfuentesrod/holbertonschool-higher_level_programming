#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    if args:
        total = sum(int(arg) for arg in args)
        print(total)
    else:
        print(0)
