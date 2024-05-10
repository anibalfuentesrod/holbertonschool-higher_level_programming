#!/usr/bin/python3
a = 1
b = 2

from add_0 import add

if __name__ == "__main__":
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
