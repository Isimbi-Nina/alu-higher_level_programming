#!/usr/bin/python3
"""Module that safely prints an integer, reporting errors to stderr."""
import sys


def safe_print_integer_err(value):
    """Print a value as an integer using "{:d}".format().

    Args:
        value: the value to print, can be of any type.

    Returns:
        True if value was correctly printed as an integer.
        False otherwise, after printing the error to stderr,
        preceded by "Exception: ".
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
