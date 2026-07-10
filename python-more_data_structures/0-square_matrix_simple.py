#!/usr/bin/python3
"""Module that squares every value of a matrix."""


def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix.

    Args:
        matrix (list of lists of int): the 2 dimensional array.

    Returns:
        A new matrix of the same size, with each value squared.
    """
    return [[value ** 2 for value in row] for row in matrix]
