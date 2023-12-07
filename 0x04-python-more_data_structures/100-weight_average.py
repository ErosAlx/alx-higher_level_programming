#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    den = 0
    if my_list == []:
        return 0
    for element in my_list:
        total = total + element[0] * elem[1]
        den = den + element[1]
    return total / den
