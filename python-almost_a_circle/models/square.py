#!/usr/bin/python3


"""
* Write the class Square that inherits from Rectangle:
* In the file models/square.py
* Class Square inherits from Rectangle
* Class constructor: def __init__(self, size, x=0, y=0, id=None):
* Call the super class with id, x, y, width and height - this super
call will use the logic of the __init__ of the Rectangle class.
The width and height must be assigned to the value of size
* You must not create new attributes for this class, use all
attributes of Rectangle - As reminder: a Square is a Rectangle
with the same width and height
* All width, height, x and y validation must inherit from Rectangle
- same behavior in case of wrong data
* The overloading __str__ method should return [Square] (<id>) <x>/<y>
- <size> - in our case, width or height
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor to initialize the Square instance

        Args:
            size (int): size of the square
            x (int): coordinate of the square
            y (int): coordinate of the square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        String method that returns a value of type string

        Returns:
            str: a modified version of the str method
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Property decorator to turn the size attribute into a getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter decorator allowing to modify the value of size
        Args:
            value (int): new value that defines the size
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
