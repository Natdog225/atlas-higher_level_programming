#!/usr/bin/python3
"""Module that contains the student class"""


class Student:
    """A class representing a student of a generic variety"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance.

        Args:
        first_name (str): First name
        last_name (str): The last name of student.
        age (int): The age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            """Retrieves a dictionary representation of Student.

            Args:
            attrs (list):
            A list of string representing the attrs to retrieve.

            Returns:
            A dictionary representation of the Student instance.
            if attrs is none, all attrs retrieved.
            if attrs is a list of strings only those are.
            """
            if attrs is None:
                return self.__dict__
            else:
                return {
                    key: value for key, value in self.__dict__.items() if key in attrs
                }

            def reload_from_json(self, json):
                """Replaces all attrs of Student instance.

                Args:
                json (dict): A dictionary containing new attr values
                """
                for key, value in json.items():
                    setattr(self, key, value)
