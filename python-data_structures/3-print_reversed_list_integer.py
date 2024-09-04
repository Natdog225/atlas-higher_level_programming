#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order.

    Args:
        my_list: The list of integers to print.
    """
    if my_list:  # Check if the list is not empty
        for i in reversed(my_list):
            print("{:d}".format(i))
