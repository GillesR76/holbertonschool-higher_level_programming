#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_key = [key for key, val in a_dictionary.items() if val == value]
    return {key: val for key, val in a_dictionary.items()
            if key not in del_key}
