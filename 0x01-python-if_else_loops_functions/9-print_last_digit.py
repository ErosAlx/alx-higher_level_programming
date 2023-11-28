#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        number = number % 10
        print("{:d}".format(number), end="")
    elif number < 0:
        number = (number % -10) * -1
        print("{:d}".format(number), end="")
        return number
