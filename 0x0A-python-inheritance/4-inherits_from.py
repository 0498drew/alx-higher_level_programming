#!/usr/bin/python3
"""Defines class checking"""


def inherits_from(obj, a_class):
    """Checking the right instance

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
