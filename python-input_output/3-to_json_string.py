#!/usr/bin/python3
"""Module that contains the to_json_string function"""
import json


def to_json_string(my_obj):
	"""Returns the JSON representation of an object

	Args:
	my_obj: The object to be converted

	Returns:
	The json string representation.
	"""
	return json.dumps(my_obj)
