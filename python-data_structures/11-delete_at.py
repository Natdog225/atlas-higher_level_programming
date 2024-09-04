#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list.

    Args:
        my_list: The list to modify.
        idx: The index of the item to delete.

    Returns:
        The modified list if the index is valid, otherwise the original list.
    """

    if 0 <= idx < len(my_list):
        del my_list[idx]  # Delete the item at the specified index

    return my_list
