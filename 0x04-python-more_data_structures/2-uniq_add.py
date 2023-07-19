#!/usr/bin/python3
def is_exist(end_idx, val, my_list=[]):
    for i in range(0, end_idx):
        if my_list[i] == val:
            return True
    return False


def uniq_add(my_list=[]):
    if my_list is None:
        return None
    sum = 0
    for i in range(0, len(my_list)):
        if is_exist(i, my_list[i], my_list) is False:
            sum += my_list[i]
    return sum
