# atlas-higher_level_programming
#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a given divisor.
"""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
    matrix (list of lists): The matrix to divide.
    div (int or float): The divsor.

    Raises:
    TypeError:
    If 'matrix' is not a list of ints/floats.
    If each row of the 'matrix' is not the same size.
    If 'div' is not a number (int or float).
    ZeroDivisionError: If 'div' is 0

    Returns:
    list of lists: A new matrix with all elements
    divided by 'div', rounded to 2 decimal places.
    """