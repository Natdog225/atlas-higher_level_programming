#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples element-wise.

    Args:
        tuple_a: The first tuple.
        tuple_b: The second tuple.

    Returns:
        A new tuple with the sum of corresponding elements.
    """

    # Ensure tuples have at least 2 elements, padding with 0 if necessary
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    # Calculate the sum of elements
    sum1 = a1 + b1
    sum2 = a2 + b2

    return (sum1, sum2)  
