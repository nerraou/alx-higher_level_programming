#!/usr/bin/python3
"""import json package """
import json
""" load json from file"""


def load_from_json_file(filename):
    """from file to json"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
