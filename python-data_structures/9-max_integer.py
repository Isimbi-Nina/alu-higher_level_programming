#!/usr/bin/python3
"""Module that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    """Return the biggest integer of a list, or None if empty."""
    if len(my_list) == 0:
        return None
    biggest = my_list[0]
    for value in my_list:
        if value > biggest:
            biggest = value
    return biggest
