#!/usr/bin/python3
"""
Module containing the `Rectangle` class
"""
from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class, inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a `Rectangle` object

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x coordinate of the rectangle
            y (int): The y coordinate of the rectangle
            id (int): The id of the rectangle.
              If `None`, an auto-incrementing id is assigned
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute

        Args:
            value (int): The new width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute

        Args:
            value (int): The new height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute

        Args:
            value (int): The new x value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute

        Args:
            value (int): The new y value
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle to stdout using '#'
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle

        Args:
            *args: Variable length argument list
            **kwargs: Keyword arguments
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle
        """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
