#!/usr/bin/python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """A class with an area method that raises an exception."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")
