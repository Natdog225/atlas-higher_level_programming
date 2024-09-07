#!/usr/bin/python3
"""
This module defines a class 'Square' representing a square shape with a private size attribute and input validation.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square's side.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square object.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        