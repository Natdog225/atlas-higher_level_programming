#!/usr/bin/python3
"""Defines the is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if an object is an exact instance of a specified class

    Args:
        obj: The object to be checked
        a_class: The class to compare against

    Returns:
        True if obj is an exact instance of a_class, False otherwise
    """
    return type(obj) == a_class
