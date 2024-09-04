#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:  # Check if dictionary is None or empty
        return None

    best_key = None
    max_score = float('-inf')

    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            best_key = key

    return best_key
