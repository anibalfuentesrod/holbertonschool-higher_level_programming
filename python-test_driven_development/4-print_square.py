#!/usr/bin/python3
def print_square(size):
    """Print a square with the char #
    
    Args:
        size (int): THe size len of the square.
    Raises:
        TypeError: If size is not an in
        ValueError: If size is negative
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        print("#" * size)
