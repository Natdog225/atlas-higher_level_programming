#!/usr/bin/python3
"""
This module defines a class 'Square' with a private size attribute.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square's side.
    """

    def __init__(self, size):
        """
        Initializes a new Square object.

        Args:
            size (int): The size of the square's side.
        """
        self.__size = size
