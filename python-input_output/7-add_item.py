#!/usr/bin/python3
"""Script to add args to a python list and save them to a JSON file"""

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

    my_list.extend(sys.argv[1:])  # adds the args to list
    save_to_json_file(my_list, filename)
