#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new line after this char

    Args:
        text (str): the text to print
    Raises:
        TypeError: if tezt is not str
    """
    if not isinstance(text, str):
        raise TypeError("text musssssst be a string")

    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1

    while char < len(text):
        print(text[char], end="")
        if text[char] == "\n" or text[char] in ".?:":
            if text[char] in ".?:":
                print("\n")
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
