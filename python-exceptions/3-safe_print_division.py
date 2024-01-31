#!/usr/bin/python3
def safe_print_division(a, b):
    calculate = None
    try:
        calculate = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(calculate))
    return calculate
