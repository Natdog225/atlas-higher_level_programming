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
            id (int): The id of the object.
              If `None`, an auto-incrementing id is assigned
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(json.dumps(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string

        Args:
            json_string (str): A JSON string representation
              of a list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

def to_json_string(list_dictionaries):
    """
    Returns the JSON string representation of list_dictionaries

    Args:
        list_dictionaries (list): A list of dictionaries
    """
    if list_dictionaries is None or list_dictionaries == []:
        return "[]"
    return json.dumps(list_dictionaries)
