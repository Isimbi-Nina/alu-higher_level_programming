#!/usr/bin/python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, space separated per row."""
    for row in matrix:
        first = True
        for value in row:
            if not first:
                print(" ", end="")
            print("{:d}".format(value), end="")
            first = False
        print()
