#!/usr/bin/python3


"""
* Write a function that writes an Object to
a text file, using a JSON representation:
* Prototype: def save_to_json_file(my_obj, filename):
* You must use the with statement
* You dont need to manage exceptions if the object cant be serialized.
* You dont need to manage file permission exceptions.
"""

import json


def load_from_json_file(filename):
    """Function that writes an Object to a text file"""
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
