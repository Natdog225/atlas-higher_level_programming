#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the biggest integer of a list.

    Args:
        my_list: The list of integers.

    Returns:
        The biggest integer in the list, or None if the list is empty.
    """

    if not my_list:  # Check if the list is empty
        return None

    max_value = my_list[0]  # Initialize max_value

    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value
