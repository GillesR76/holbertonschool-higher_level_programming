#!/usr/bin/python3
def safe_print_division(a, b):
    calculate = 0
    try:
        calculate = a / b
        if a and b > 0:
            print("Inside result: {}".format(float(calculate)))
    except Exception:
        print("Inside result: None")
        pass
    finally:
        if a and b > 0:
            return calculate
