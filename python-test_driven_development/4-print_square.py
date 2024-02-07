#!/usr/bin/python3
"""
Write a function that prints a square with the character #
Size must be an integer otherwise raise a TypeError
Size must be >= 0 otherwise raise a ValueError
Size must not be a float and < 0 otherwise raise a Type Error
Prints a square of size size
"""


def print_square(size):
    """
    Function that prints a square with the character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for x in range(size):
            print("#" * size)
