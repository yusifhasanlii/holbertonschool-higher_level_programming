#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = None
    try:
        res = fct(*args)
        return res
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
