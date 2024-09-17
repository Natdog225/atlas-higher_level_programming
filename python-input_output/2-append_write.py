#!/usr/bin/python3
"""Module that contains append_write function"""

def append_write(filename="", text=""):
	"""Appends a string at the end of a text file and returns number
	of characters added

	Args:
	Filename (str): The name of the file to append
	text (str): The string to append to the file

	Returns:
	The number of characters added
	"""
	with open(filename, mode="a", encoding="utf-8") as f:
		return f.write(text)
