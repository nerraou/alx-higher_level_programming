#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    if my_list is None:
        return
    if (x < 0):
        return 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
    except IndexError:
        i -= 1
    if i > 0:
        print("")
    return i + 1
