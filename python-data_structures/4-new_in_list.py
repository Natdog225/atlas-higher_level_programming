#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position without modifying the original list.

    Args:
        my_list: The original list.
        idx: The index of the element to replace.
        element: The new element to be inserted.

    Returns:
        A new list with the element replaced if the index is valid, otherwise it gives a copy of the original list.
    """

    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Return a copy of the original list if the index is invalid

    new_list = my_list.copy()  # Create a copy of the original list
    new_list[idx] = element    # Replace the element at the specified index
    return new_list
