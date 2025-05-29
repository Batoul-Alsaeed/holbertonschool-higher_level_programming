#!/usr/bin/python3
"""
Check if object inherits from a class (but is not exactly that class)
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj inherits from a_class (directly or indirectly)
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
