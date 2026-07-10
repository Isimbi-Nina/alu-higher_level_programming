#!/usr/bin/python3
"""Module that returns length and first character of a string."""


def multiple_returns(sentence):
    """Return a tuple with the length of sentence and its first char."""
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
