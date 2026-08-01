#!/usr/bin/python3
"""Module that defines a class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description of obj for JSON serialization.

    Args:
        obj: an instance of a class whose attributes are all
            serializable (list, dictionary, string, integer, boolean).

    Returns:
        dict: a dictionary representation of obj's attributes.
    """
    return obj.__dict__
