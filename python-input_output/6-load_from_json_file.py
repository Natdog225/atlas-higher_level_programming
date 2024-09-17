#!/usr/bin/python3
"""Module containing load_from_json_file function"""

import json


def load_from_json_file(filename):
    """Creates an object from JSON file

    Args:
    filename (str): The name of the
    JSON file to read from

    returns:
    The python object represented
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
