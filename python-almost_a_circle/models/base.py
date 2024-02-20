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
        """Staticmethod that writes the JSON string representation
        of list_objs to a file
        """
        if not json_string or json_string is None:
            json_string = []
            return json_string
        return json.loads(json_string)
