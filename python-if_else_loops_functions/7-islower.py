#!/usr/bin/python3

def islower(c):
    """Checks if a character is lowercase.

    Args:
        c: The character to check.

    Returns:
        True if c is lowercase, False otherwise.
    """

    return ord(c) >= 97 and ord(c) <= 122
