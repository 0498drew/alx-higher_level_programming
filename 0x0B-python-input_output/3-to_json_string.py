#!/usr/bin/python3
"""Defining JSON presentation of an object string"""
import json


def to_json_string(my_obj):
    """Return json presentation.

    arg:
        my_obj(): a string of an object
    results
        json presentation
    """
    return json.dumps(my_obj)
