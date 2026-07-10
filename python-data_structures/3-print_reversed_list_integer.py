#!/usr/bin/python3
"""Module that prints all integers of a list, in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order, one per line."""
    i = len(my_list) - 1
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i -= 1
