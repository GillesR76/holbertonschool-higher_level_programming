#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_newlist = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_newlist
    my_newlist[idx] = element
    return my_newlist
