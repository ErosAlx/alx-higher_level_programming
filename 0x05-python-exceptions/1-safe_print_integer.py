#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        None
        print(value, "is not an integer")
    return True
