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
        self.__size = size

    @property
    def size(self):
        """
        Property decorator to turn the size method into a getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter decorator allowing to modify the value of size method

        Args:
            value (int): new value that defines the size of the square
        """
        if not isinstance(value, int):
            """
            Raising a TypeError exception as the size/value must be an integer
            """
            raise TypeError("size must be an integer")
        elif value < 0:
            """
            Raising a ValueError exception as the size/value must be >= 0
            """
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Public instance method that returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Public instance method that prints the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for x in range(0, self.__size):
                for y in range(0, self.__size):
                    print("#", end="")
                print()
