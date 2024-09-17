#!/usr/bin/python3
"""Module that contains the from_json_string"""

import json


def from_json_string(my_str):
	"""Returns an object (like a data structure) represented by JSON string

	Args:
	my_str (str): The JSON string to be converted to an object

	Returns:
	The python object represented
	"""
	return json.loads(my_str)