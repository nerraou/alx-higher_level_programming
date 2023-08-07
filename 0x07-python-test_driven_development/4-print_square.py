#!/usr/bin/python3
"""Module for print_square function"""


def print_square(size):
    """print square"""

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        print("#" * size)
