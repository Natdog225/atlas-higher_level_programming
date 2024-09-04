#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.

    Args:
        matrix: The matrix to print (a list of lists of integers).
    """

    for row in matrix:
        for i, num in enumerate(row):  # Use enumerate to get index and value
            print("{:d}".format(num), end=" " if i < len(row) - 1 else "")  # Print space between elements, except for the last one in a row
        print()
