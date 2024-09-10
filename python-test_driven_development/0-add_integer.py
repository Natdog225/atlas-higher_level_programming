#!/usr/bin/python3
"""
This module provides a function to add two ints
"""


def add_integer(a, b=98):
    """
    Adds two ints or floats after converting floats to ints

    Args:
    a (int or float) the first number to add
    b (int or float) The second number to add defaults to 98]

    Raises:
    TypeError: if either 'a' or 'b' is not an integer

    Returns:
    int: the of 'a' and 'b'.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
