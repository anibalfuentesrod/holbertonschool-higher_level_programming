#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if character is a lowercase letter
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
            # Convert lowercase letter to uppercase by subtracting 32 from Ascii
            print("{}".format(char), end="")
