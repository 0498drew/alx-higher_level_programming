#!/usr/bin/python3
"""Defining a func that write object string file in json representation"""
import json


def save_to_json_file(my_obj, filename):
    """write an object string file in json representation

    arg:
        my_obj: object to be written
        filename: file to be written on
    results:
        written obj
    """
    with open(filename, 'w') as f:
        return json.dumps(my_obj)
