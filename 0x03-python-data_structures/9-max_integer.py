#!/usr/bin/python3
def max_integer(my_list=[]):
    lenght = len(my_list)
    if my_list is None or lenght == 0:
        return None
    max_val = my_list[0]
    for i in range(1, lenght):
        val = my_list[i]
        if max_val < val:
            max_val = val
    return max_val
