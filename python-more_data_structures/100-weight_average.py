#!/usr/bin/python3
"""Module that computes the weighted average of a list of tuples."""


def weight_average(my_list=[]):
    """Return the weighted average of a list of (score, weight) tuples.

    Args:
        my_list (list): list of (score, weight) tuples.

    Returns:
        The weighted average as a float, or 0 if the list is empty.
    """
    if not my_list:
        return 0

    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for score, weight in my_list)

    if total_weight == 0:
        return 0

    return total_score / total_weight
