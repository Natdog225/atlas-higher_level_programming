#!/usr/bin/python3
"""Module that contains the pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n

    Args:
        n (int): The number of rows in the triangle

    Returns:
        A list of lists representing Pascal's triangle
    """

    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        row = [1]  # Each row starts with 1
        prev_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Each row ends with 1
        triangle.append(row)  # Append the completed row to the triangle

    return triangle
