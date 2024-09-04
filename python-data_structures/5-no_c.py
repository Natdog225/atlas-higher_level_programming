#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters 'c' and 'C' from a string.

    Args:
        my_string: The string to process.

    Returns:
        The new string without 'c' or 'C'.
    """

    new_string = ""
    for char in my_string:
        if char.lower() != 'c':  # Check if the character is not 'c'
            new_string += char    # Append the character to the new string

    return new_string
