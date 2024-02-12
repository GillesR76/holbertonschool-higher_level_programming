#!/usr/bin/python3


"""
* Write a function that returns the list of available
attributes and methods of an object
* Returns a list object
* You are not allowed to import any module
"""


def lookup(obj):
    """
    Function that returns the list of available
    attributes and methods of an object
    """
    return dir(obj)
