#!/usr/bin/python3
"""
Module containing the `Base` class
"""
import json


class Base:
    """
    The Base class from which other classes will inherit
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a `Base` object

        Args:
            id (int): The id of the object. If `None`, an auto id is assigned
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
