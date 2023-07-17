#!/usr/bin/python3
def get_value(idx, tuple_c=()):
    length = len(tuple_c)
    if length <= idx:
        return 0
    return tuple_c[idx]


def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return None
    sum1 = get_value(0, tuple_a) + get_value(0, tuple_b)
    sum2 = get_value(1, tuple_a) + get_value(1, tuple_b)
    tuple_c = (sum1, sum2)
    return tuple_c
