#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        if fct(*args):
            return fct(*args)
    except Exception:
        print("Exception: list index out of range",
              file=sys.stderr)
        return None
