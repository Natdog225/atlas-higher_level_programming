#!/usr/bin/python3
"""
Module containing the `Square` class
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The Square class, inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a `Square` object

        Args:
            size (int): The size of the square
            x (int): The x coordinate of the square
            y (int): The y coordinate of the square
            id (int): The id of the square. If `None`, an auto-incrementing id is assigned
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """
        Getter for the size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute

        Args:
            value (int): The new size value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square

        Args:
            *args: Variable length argument list
            **kwargs: Keyword arguments
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    if attrs[i] == "size":
                        self.size = arg
                    else:
                        setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    if key == "size":
                        self.size = value
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
