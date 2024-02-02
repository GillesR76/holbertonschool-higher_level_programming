#!/usr/bin/python3
"""
Write an empty class Square that defines a square by:
* Private instance attribute: size
* Instantiation with size (no type/value verification)
* You are not allowed to import any module
"""


class Square:
    """
    Class named Square
    """
    def __init__(self, size=0):
        """
        Use of the init method to create a private instance attribute: size

        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            """
            Raising a TypeError exception as size must be an integer
            """
            raise TypeError("size must be an integer")
        elif size < 0:
            """
            Raising a ValueError exception as size must be >= 0
            """
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Public instance method that returns the current square area
        """
        return self.__size ** 2
