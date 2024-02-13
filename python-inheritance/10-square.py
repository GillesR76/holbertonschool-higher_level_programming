#!/usr/bin/python3


"""
* Write a class BaseGeometry
* Public instance method: that raises an Exception
* Public instance method that validates value
* You are not allowed to import any module
"""


class BaseGeometry:
    """class 'BaseGeometry'"""

    def area(self):
        """Public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """New class Rectangle that inherits from parent class"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Public instance method inherited from parent class"""
        return self.__width * self.__height

    def __str__(self):
        """String method"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """New subclass Square that inherits from subclass Rectangle"""

    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Public instance method inherited from parent class"""
        return self.__size * self.__size

    def __str__(self):
        """String method"""
        return f"[Rectangle] {self.__size}/{self.__size}"
