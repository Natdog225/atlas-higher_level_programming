#!/usr/bin/python3
"""Module that contains the student class"""


class Student:
    """A class for student"""

    def __init__(self, first_name, last_name, age):
        """Initializes student

        Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student instance

        Args:
        attrs (list): A list of strings representing the attributes
        to retrieve.

        Returns: A dictionary of the student instance.
        if attrs is none, all are retrieved
        if attrs is a list of strings, only those attrs are retrieved.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key
                    in attrs}
