#!/usr/bin/python3
""" append file """


def append_write(filename="", text=""):
    """ write into file"""
    with open(filename, "a", encoding="utf-8") as f:
        write_data = f.write(text)
    return write_data
