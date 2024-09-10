#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix
by a given divisor.
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

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("Division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

        return new_matrix
