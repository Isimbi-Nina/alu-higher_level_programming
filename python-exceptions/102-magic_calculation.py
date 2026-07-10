#!/usr/bin/python3
"""Module reproducing a given Python bytecode as a function."""


def magic_calculation(a, b):
    """Perform the calculation described by the provided bytecode.

    Args:
        a: a numeric value.
        b: a numeric value.

    Returns:
        The computed result.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
