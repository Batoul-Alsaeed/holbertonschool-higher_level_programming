#!/usr/bin/python3
"""Module that defines a Student class with serialization and reloading."""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of instance.
        If attrs is a list of strings, only those attributes are returned.
        Otherwise, all attributes are returned."""
        if isinstance(attrs, list) and all(type(attr) == str for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance using a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
