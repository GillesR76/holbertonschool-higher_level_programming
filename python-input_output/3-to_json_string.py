#!/usr/bin/python3


"""
* Write a function that returns the JSON representation
of an object (string):
* Prototype: def to_json_string(my_obj):
* You dont need to manage exceptions if
the object cant be serialized.
"""

import json


def to_json_string(my_obj):
    """Function that returns a json representation"""
    return json.dumps(my_obj)
