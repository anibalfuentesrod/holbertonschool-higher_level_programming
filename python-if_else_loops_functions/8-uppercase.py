#!/usr/bin/python3
def uppercase(str):
    for char in str:
        assci_value = ord(char)
        # Check if character is a lowercase letter
        if 97 <= assci_value <= 122:
            # Convert lowercase letter to uppercase by subtracting 32 from Ascii
            print("{} ".format(chr(assci_value - 32)), end="")
        else:
            print(char, end="")
