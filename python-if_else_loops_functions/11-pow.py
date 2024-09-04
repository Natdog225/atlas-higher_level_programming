#!/usr/bin/python3

def pow(a, b):
    """Computes a to the power of b and returns the value.

    Args:
        a: The base number.
        b: The exponent.

    Returns:
        The value of a raised to the power of b.
    """

    result = 1
    if b == 0:
        return result  # Any number to the power of 0 is 1

    if b < 0:
        a = 1 / a  # Handle negative exponents
        b = -b

    for _ in range(b):
        result *= a

    return result
