#!/usr/bin/python3

def print_last_digit(number):
    """Prints the last digit of a number.

    Args:
        number: The number to process.

    Returns:
        The value of the last digit.
    """

    last_digit = abs(number) % 10  # Get the absolute value and then the remainder when divided by 10
    print(last_digit, end="")
    return last_digit
