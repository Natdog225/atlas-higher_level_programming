#!/usr/bin/python3
"""
This module defines a class 'Square' representing a square shape with a private size attribute, input validation, an area calculation method, getter/setter properties for size and position, and a method to print the square using '#' with positioning.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square's side.
        __position (tuple): The position of the square (x, y coordinates).

    Properties:
        size (int): Gets or sets the size of the square's side with validation.
        position (tuple): Gets or sets the position of the square with validation.

    Methods:
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square using '#' characters with positioning.

    Raises:
        TypeError: 
            - If the assigned `size` is not an integer.
            - If the assigned `position` is not a tuple of 2 positive integers.
        ValueError: If the assigned `size` is less than 0.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square object.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.
            position (tuple, optional): The position of the square (x, y coordinates). Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            tuple: The position of the square (x, y coordinates).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): The new position to set (x, y coordinates).

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters with positioning.

        If size is 0, prints an empty line.
        Uses spaces for positioning based on the `position` attribute.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):  # Print empty lines for y-coordinate
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)  # Print spaces for x-coordinate
            