#!/usr/bin/python3
"""Module containing lookup function"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

    Args:
        obj: The object whose stuff should be listed

    Returns:
        A list containing the names of attributes and methods
    """
    return dir(obj)
