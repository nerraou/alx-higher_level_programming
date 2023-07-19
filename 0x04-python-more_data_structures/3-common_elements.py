#!/usr/bin/python3
def is_exist(val, my_list=[]):
    for x in my_list:
        if x == val:
            return True
    return False


def common_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return None
    new_set = []
    for x in set_1:
        if is_exist(x, set_2) is True:
            new_set.append(x)
    return new_set
