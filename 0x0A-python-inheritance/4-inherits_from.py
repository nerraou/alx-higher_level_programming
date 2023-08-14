#!/usr/bin/python3
"""
check is inherits from
"""


def inherits_from(obj, a_class):
    """
     check is an instance
    of class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
