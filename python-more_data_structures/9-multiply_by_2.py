#!/usr/bin/python3
"""Module that multiplies all values of a dictionary by 2."""


def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): the dictionary whose values are integers.

    Returns:
        A new dictionary with each value doubled.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
