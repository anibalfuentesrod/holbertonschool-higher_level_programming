#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10 if number >= 0 else ((number * -1) % 10) * -1

if last > 5:
    output = 'Last digit of {} is {} and is greater than 5'.format(number, last)

elif last < 6 and last != 0:
    output = 'Last digit of {} is {} and is less than 6 and not 0'.format(number, last)

elif last == 0:
    output = 'Last digit of {} is {} and is 0'.format(number, last)

print(output)
