#!/usr/bin/python3


"""
* Write a function that returns the JSON representation
of an object (string):
* Prototype: def to_json_string(my_obj):
* You dont need to manage exceptions if
the object cant be serialized.
"""

import json


def from_json_string(my_str):
    """Function that returns a json representation"""
    return json.loads(my_str)
