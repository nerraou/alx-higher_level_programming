#!/usr/bin/python3
"""save args to file"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

out_filename = "add_item.json"
sys.argv.pop(0)
save_to_json_file(sys.argv, out_filename)
