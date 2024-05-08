#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10 if number >= 0 else ((number * -1) % 10) * -1
prefix = "Last digit of"
if last > 5:
    output = "{} {} is {} and is greater than 5".format(prefix, number, last)

elif last < 6 and last != 0:
    output = ("{} {} is {} and is less than 6 "
    "and not 0".format(prefix, number, last))

elif last == 0:
    output = "{} {} is {} and is 0".format(prefix, number, last)

print(output)
