#!/usr/bin/python3
"""save args to file"""
import sys
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":

    filename = "add_item.json"
    if os.path.isfile(filename):
        values = load_from_json_file(filename)
    else:
        values = []

    sys.argv.pop(0)

    values.extend(sys.argv)

    save_to_json_file(values, filename)
