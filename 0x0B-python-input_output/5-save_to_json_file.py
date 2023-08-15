#!/usr/bin/python3
"""import json package """
import json
""" return save json to file"""


def save_to_json_file(my_obj, filename):
    """from json to file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
