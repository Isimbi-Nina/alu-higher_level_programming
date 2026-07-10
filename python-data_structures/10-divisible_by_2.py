#!/usr/bin/python3
"""Module that finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    """Return a new list of booleans indicating multiples of 2."""
    result = []
    for value in my_list:
        result.append(value % 2 == 0)
    return result
