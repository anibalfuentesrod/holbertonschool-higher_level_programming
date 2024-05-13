#!/usr/bin/python3
def no_c(my_string):
    result = ''
    for c in my_string:
        if c != 'c' and c != 'C':
            result += c
    return result
