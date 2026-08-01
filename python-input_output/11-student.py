#!/usr/bin/python3
"""Module that defines the Student class."""


class Student:
    """Class that represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the student's first name.
            last_name (str): the student's last name.
            age (int): the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list): optional list of attribute names (strings) to
                retrieve. If not a list of strings, all attributes of
                the instance are retrieved.

        Returns:
            dict: a filtered or complete dictionary of the student's
                attributes.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dict.

        Args:
            json (dict): a dictionary whose keys are attribute names
                and whose values are the values to set on the instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
