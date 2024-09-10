#!/usr/bin/python3
"""
This module provides a function to print text with indentation after specific characters.
"""


def text_indentation(text):
    """
    Prints text with two new lines after each of these characters: '.', '?', and ':'.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n")

    lines = text.splitlines()
    for line in lines:
        print(line.strip())