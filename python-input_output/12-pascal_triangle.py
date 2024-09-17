#!/usr/bin/python3
"""Module that contains the pascal_triangle function"""

def pascal_triangle(n):
	"""Returns a list of lists of ints that might resemble Pascal's
	triangle.

	Args: n (int): The number of rows in the triangle

	Returns:
	A list of list resembling a triangle.
	"""

	if n <= 0:
		return []
	
	triangle = [[1]]

	for i in range(1, n):
		row = [1]
		prev_row = triangle[i - 1]
		for j in range(1, i):
			row.append(prev_row[j - 1] + prev_row[j])
			row.append(1)
			triangle.append(row)

		return triangle

