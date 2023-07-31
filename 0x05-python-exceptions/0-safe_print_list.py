#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return
    i = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
    except IndexError:
        i = i - 1
    print("")
    return i + 1
