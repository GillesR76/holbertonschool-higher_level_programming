#!/usr/bin/python3


"""
* Write the class Rectangle that inherits from Base:
* In the file models/rectangle.py
* Class Rectangle inherits from Base
* Private instance attributes, each with its own
public getter and setter:
__width -> width
__height -> height
__x -> x
__y -> y
* Class constructor: def __init__(self, width, height,
x=0, y=0, id=None):
* Call the super class with id - this super call with
use the logic of the __init__ of the Base class
* Assign each argument width, height, x and y to the right attribute
"""

from models.base import Base


class Rectangle(Base):
    """Sublclass of Base named Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor to initialize the Rectanble instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): coordinate of the rectangle
            y (int): coordinate of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Property decorator to turn the width attribute into a getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter decorator allowing to modify the value of width
        Args:
            value (int): new value that defines the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Property decorator to turn the height attribute into a getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter decorator allowing to modify the value of width
        Args:
            value (int): new value that defines the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Property decorator to turn the x attribute into a getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter decorator allowing to modify the value of width
        Args:
            value (int): new value that defines x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Property decorator to turn the y attribute into a getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter decorator allowing to modify the value of width
        Args:
            value (int): new value that defines y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public method that returns the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """Public method that prints the rectangle in stdout"""
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        String method that returns a value of type string

        Returns:
            str: a modified version of the str method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
