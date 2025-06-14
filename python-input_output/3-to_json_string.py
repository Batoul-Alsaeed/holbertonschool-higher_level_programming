#!/usr/bin/python3
"""Module that provides a function to convert object to JSON string."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object as a string."""
    return json.dumps(my_obj)
