#!/usr/bin/python3
"""save args to file"""
from sys import argv
"""save json to file"""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
"""load json from file"""
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    values = load_from_json_file(filename)
except FileNotFoundError:
    values = []

sys.argv.pop(0)

values.extend(sys.argv)

save_to_json_file(values, filename)
