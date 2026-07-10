#!/usr/bin/python3
"""Module that safely prints an integer."""


def safe_print_integer(value):
    """Print an integer using the "{:d}".format() syntax.

    Args:
        value: the value to print, can be of any type.

    Returns:
        True if value was correctly printed as an integer,
        False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
