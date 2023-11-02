#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    find first peak
    """
    i = 1
    length = len(list_of_integers)
    if length == 0:
        return None
    if length == 1:
        return list_of_integers[0]
    if length >= 2 and list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[length - 1] >= list_of_integers[length - 2]:
        return list_of_integers[length - 1]
    prev = list_of_integers[0]
    cur = 0
    for i in range(length - 1):
        cur = list_of_integers[i]
        if cur >= list_of_integers[i + 1] and cur >= prev:
            return list_of_integers[i]
        prev = cur
