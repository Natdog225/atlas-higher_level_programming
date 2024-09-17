#!/usr/bin/python3
"""Module that contains the class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description with data structure (list,
    dictionary, string, integer and boolean) for JSON serialization

    Args:
    obj: An instance of a class

    Returns:
    A dictionary description of object
    """
    return obj.__dict__
