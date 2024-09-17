#!/usr/bin/python3
"""Module containing save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON

    Args:
    my_obj: The object to be written to the file
    filename (str): The name of the file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
