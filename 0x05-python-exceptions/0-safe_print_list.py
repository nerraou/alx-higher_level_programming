#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0

    if (x < 0):
        print("")
        return 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
    except IndexError:
        i -= 1
    print("")
    return i + 1
