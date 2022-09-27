#!/usr/bin/python3
"""Defines instance class checking"""


def is_kind_of_class(obj, a_class):
    """Checking the inheretied instance.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
