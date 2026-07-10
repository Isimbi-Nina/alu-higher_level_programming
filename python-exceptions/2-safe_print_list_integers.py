#!/usr/bin/python3
"""Module that prints and counts integers in a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list, only if they are integers.

    Non-integer elements are skipped silently. If x is bigger than the
    length of my_list, an IndexError is expected to occur and propagate.

    Args:
        my_list (list): the list to print elements from.
        x (int): the number of elements to access in my_list.

    Returns:
        The real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
