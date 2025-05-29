#!/usr/bin/python3
"""Function that adds new attribute to an object if allowed"""


def add_attribute(obj, attr_name, value):
    """Adds new attribute to an object if possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
