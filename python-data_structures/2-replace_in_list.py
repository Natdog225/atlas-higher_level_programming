#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position.

    Args:
        my_list: The list to modify.
        idx: The index of the element to replace.
        element: The new element to insert.

    Returns:
        The modified list if the index is valid, otherwise the original list.
    """

    if 0 <= idx < len(my_list):  # Check if idx is within valid bounds
        my_list[idx] = element 

    return my_list  # Return the (potentially modified) list
