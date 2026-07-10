#!/usr/bin/python3
"""Module that divides two integers and prints the result."""


def safe_print_division(a, b):
    """Divide a by b and print the result inside a finally block.

    Args:
        a (int): the dividend.
        b (int): the divisor.

    Returns:
        The result of the division, or None if the division failed.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
