#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == "__main__":
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))

    result = sub(a, b)
    print("{} - {} = {}".format(a, b, result))

    result = mul(a, b)
    print("{} * {} = {}".format(a, b, result))

    result = div(a, b)
    print("{} / {} = {}".format(a, b, result))
