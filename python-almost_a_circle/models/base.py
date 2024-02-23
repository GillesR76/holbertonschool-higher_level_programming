#!/usr/bin/python3


"""
* Write the first class Base:
* Create a folder named models with an empty file __init__.py
inside - with this file, the folder will become a Python package
* Create a file named models/base.py:
* Class Base:
* private class attribute __nb_objects = 0
* class constructor: def __init__(self, id=None)::
* if id is not None, assign the public instance attribute id with this
argument value you can assume id is an integer and you dont need to
test the type of it
* otherwise, increment __nb_objects and assign the new value
to the public instance attribute id
"""

import json
import os.path
import turtle


class Base:
    """
    Class named Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Using the init method to initialize public instance attributes
        and private class attributes

        Args:
        id
        """
        self.id = id
        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the json string
        representation of the object
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Classmethod that writes the JSON string representation
        of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Staticmethod that that returns the list of the
        JSON string representation to an object
        """
        if not json_string or json_string is None:
            json_string = []
            return json_string
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with all attributes
        already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 0, 0, None)
        elif cls.__name__ == "Square":
            dummy = cls(1, 0, 0, None)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances
        from a file
        """
        file_of_instances = cls.__name__ + ".json"
        if not os.path.isfile(file_of_instances):
            return []
        with open(file_of_instances, "r") as f:
            file_to_string = f.read()
        list_of_instances = cls.from_json_string(file_to_string)
        dict_instances = [cls.create(**dict) for dict in list_of_instances]
        return dict_instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        my_turtle = turtle.Turtle()
        my_turtle.speed(1)
        for rectangle in list_rectangles:
            my_turtle.color('yellow', 'green')
            my_turtle.penup()
            my_turtle.goto(rectangle.x, rectangle.y)
            my_turtle.pendown()
            my_turtle.begin_fill()
            for _ in range(2):
                my_turtle.forward(rectangle.width)
                my_turtle.right(90)
                my_turtle.forward(rectangle.height)
                my_turtle.right(90)
            my_turtle.end_fill()

        for square in list_squares:
            my_turtle.color('red', 'purple')
            my_turtle.begin_fill()
            for _ in range(4):
                my_turtle.forward(square.size)
                my_turtle.right(90)
            my_turtle.end_fill()

        turtle.done()
