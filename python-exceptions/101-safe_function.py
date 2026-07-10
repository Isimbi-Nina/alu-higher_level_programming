#!/usr/bin/python3
"""Module that executes a function safely."""
import sys


def safe_function(fct, *args):
    """Execute a function safely, catching any exception it raises.

    Args:
        fct: a pointer to the function to execute.
        *args: the arguments to pass to fct.

    Returns:
        The result of fct(*args), or None if an exception occurred,
        after printing the error to stderr, preceded by "Exception: ".
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
