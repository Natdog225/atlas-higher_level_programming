#!/usr/bin/python3
"""Defines the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of or inherits from a specified class

    Args:
        obj: The object to be checked
        a_class: The class to compare against

    Returns:
        True if obj is an instance of a_class or a subclass, False otherwise
    """
    return isinstance(obj, a_class)
