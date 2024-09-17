#!/usr/bin/python3
"""Defines the MyList class, inheriting from list."""


class MyList(list):
    """A subclass of list that has a print_sorted method."""

    def print_sorted(self):
        """Prints the list elements in ascending sorted order."""
        print(sorted(self))
