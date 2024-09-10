#!/usr/bin/python3
"""
This module defines a class 'Rectangle' representing a rectangle shape with private width and height attributes, input validation, methods for calculating area and perimeter, string representations, a destructor, and a class attribute to track the number of instances
"""


class Rectangle:
    """
    A class that represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle

    Properties:
        width (int): Gets or sets the width
        height (int): Gets or sets the height

    Methods:
        area(self): Calculates and returns the area
        perimeter(self): Calculates and returns the perimeter

    Class Attributes:
        number_of_instances (int): The number of Rectangle instances

    Raises:
        TypeError: If the assigned `width` or `height` is not an integer
        ValueError: If the assigned `width` or `height` is less than 0
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value (int): The new width to set.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value (int): The new height to set

        Raises:
            TypeError: If `value` is not an integer
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area

        Returns:
            int: The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)), 
                 or 0 if either width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#' characters.

        Returns:
            str: The string representation of the rectangle, 
            or an empty string if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a formal string representation of the rectangle object

        Returns:
            str: A string that can be used to recreate the object, `Rectangle(width, height)`
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a farewell message when the Rectangle instance is deleted.
        Also decrements the number of instances
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
