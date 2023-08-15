#!/usr/bin/python3
""" write file """


def write_file(filename="", text=""):
    """ write into file"""
    with open(filename, "w", encoding="utf-8") as f:
        write_data = f.write(text)
    return write_data
