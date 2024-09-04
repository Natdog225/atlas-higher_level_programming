#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints all integers of a list, one per line.

    Args:
        my_list: The list of integers to print.
    """

    for i in my_list:
        print("{:d}".format(i))
