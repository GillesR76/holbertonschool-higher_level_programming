#!/usr/bin/python3


"""
* Write a function that creates an Object from a “JSON file”:
* Prototype: def load_from_json_file(filename):
* You must use the with statement
* You dont need to manage exceptions if the JSON string
doesnt represent an object.
* You dont need to manage file permissions / exceptions.
"""

import json


def load_from_json_file(filename):
    """Function that creates an Object from a JSON file"""
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
