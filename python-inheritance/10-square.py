#!/usr/bin/python3
"""Defines the Square class, inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
