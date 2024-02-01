#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        if fct(*args):
            return fct(*args)
    except Exception:
        if args[1] == 0:
            print("Exception: division by zero", file=sys.stderr)
        else:
            print("Exception: list index out of range",
                  file=sys.stderr)
        return None
