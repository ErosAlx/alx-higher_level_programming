#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    case = True
    try:
        print("{:d}".format(value))
    except Exception as error:
        print("Exception:", error, file=sys.stderr)
        case = False
    return case
