#!/usr/bin/python3
"""Module that contains the Student class"""


class Student:
    """A class representing a student. Just a regular ol' student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student, to school

        Args:
        first_name (str): Sometimes I feel like these are too obvious
        last_name (str): The GUESS WHAT, last name.
        age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """Retrieves a dictionary representation of a student"""
            return self.__dict__
