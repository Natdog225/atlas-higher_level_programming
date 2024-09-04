#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character.

    Args:
        sentence: The input string.

    Returns:
        A tuple containing:
            - The length of the sentence.
            - The first character of the sentence, or None if the sentence is empty.
    """

    length = len(sentence)
    first_char = sentence[0] if sentence else None

    return (length, first_char)
