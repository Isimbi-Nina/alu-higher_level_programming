#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """Class that serves as a base for geometry classes."""

    def area(self):
        """Raise an Exception since area() is not implemented."""
        raise Exception("area() is not implemented")
