#!/usr/bin/python3
"""Defines the inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited
    from the specified class

    Args:
        obj: The object to be checked
        a_class: The class to compare against

    Returns:
        True if obj is an instance of a subclass of a_class, False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
