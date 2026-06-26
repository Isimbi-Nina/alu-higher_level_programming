#!/usr/bin/python3
"""Module for magic_calculation function"""
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    """Performs a calculation based on a comparison between a and b

    Args:
        a: first integer
        b: second integer

    Returns:
        If a < b: adds a and b, then adds 4 and 5 to the result.
        Otherwise: subtracts b from a.
    """
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    return sub(a, b)
