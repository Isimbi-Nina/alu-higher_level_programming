#!/usr/bin/python3
"""Module that defines the Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that represents a square, based on Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is not greater than 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
