#!/usr/bin/python3
"""
Write a function that prints My name is <first name> <last name>
first_name and last_name must be strings otherwise, raise a TypeError
"""


def say_my_name(first_name, last_name=""):
    """
    Write a function that prints My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
