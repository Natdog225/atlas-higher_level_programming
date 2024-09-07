#!/usr/bin/python3
"""
This module defines a class 'Square' representing a square shape with a private size attribute, input validation, an area calculation method, and getter/setter properties for size.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square's side.

    Properties:
        size (int): Gets or sets the size of the square's side with validation.

    Methods:
        area(self): Calculates and returns the area of the square.

    Raises:
        TypeError: If the assigned `size` is not an integer.
        ValueError: If the assigned `size` is less than 0.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square object.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.
        """
        self.size = size  # Use the setter to validate and set the size

    @property
    def size(self):
        """
        Gets the size of the square's side.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square's side with validation.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2