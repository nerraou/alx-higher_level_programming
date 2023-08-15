#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """ read file using with """
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
