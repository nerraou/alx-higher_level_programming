#!/usr/bin/python3
"""save args to file"""


from sys import argv
"""append arguments"""
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
"""load object from JSON file"""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
"""writes an object to text file"""

filename = "add_item.json"
try:
    values = load_from_json_file(filename)
except FileNotFoundError:
    values = []

values.extend(argv[1:])
save_to_json_file(values, filename)
