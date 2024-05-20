#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>

    Args:
        first_name (str): first name
        las_name (str): last name and default ""

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print('My name is', first_name, last_name)