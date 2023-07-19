#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if my_list is None:
        return None

    def mult_by_number(x):
        return x * number

    new_list = map(mult_by_number, my_list)
    return list(new_list)
