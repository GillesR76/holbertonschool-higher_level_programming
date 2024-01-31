#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        multiply = sum([item[0] * item[1] for item in my_list])
        average = sum([item[1] for item in my_list])
    return multiply / average
