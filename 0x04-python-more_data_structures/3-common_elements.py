#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for item in set_1:
        for element in set_2:
            if item == element:
                common.append(item)
    return common
