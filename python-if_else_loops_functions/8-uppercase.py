#!/usr/bin/python3

def uppercase(str):
    """Prints a string in uppercase followed by a new line.
    Args:
        str: The string to convert and print.
    """

    result = ""  # Initialize an empty string

    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:  # Check if lowercase
            result += chr(ord(c) - 32)  # Convert to uppercase and append
        else:
            result += c  # Append non-lowercase characters as is

    print(result)g
