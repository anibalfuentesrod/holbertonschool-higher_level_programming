#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new line after this char
    
    Args:
        text (str): the text to print
    Raises:
        TypeError: if tezt is not str
    """
    if not isinstance(text, str):
        raise TypeError("text must be as string")
    
    characters = ".?:"
    result = ""
    i = 0

    while i < len(text):
        if text[i] in characters:
            result += text[i] + "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            result += text[i]
            i += 1
    
    result = result.rstrip()
    print(result + "\n", end="")
