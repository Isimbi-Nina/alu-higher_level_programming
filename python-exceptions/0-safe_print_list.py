#!/usr/bin/python3
"""Module that safely prints x elements of a list."""


def safe_print_list(my_list=[], x=0):
    """Print x elements of a list, on the same line.

    Args:
        my_list (list): the list to print elements from.
        x (int): the number of elements to print.

    Returns:
        The real number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
