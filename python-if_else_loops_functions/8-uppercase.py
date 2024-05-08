#!/usr/bin/python3
def uppercase(str):
    for char in str:
       # Check if tha char is a low letter
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert low letter to upper substracting 32 from assci
            char = chr(ord(char) - 32)
            # Print the char (either converted or unchanged)
            print("{}".format(char), end="")
            # Print a new line after printing the upper string
print("")