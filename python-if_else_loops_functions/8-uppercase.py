#!/usr/bin/python3

def uppercase(str):
    """Prints a string in uppercase followed by a new line.

    Args:
        str: The string to convert and print.
    """

    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:  # Check if lowercase
            print(chr(ord(c) - 32), end="")  # Convert to uppercase
        else:
            print(c, end="")  # Print non-lowercase characters as is
    print()  # Print a new line
