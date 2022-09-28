#!/usr/bin/python3
"""A function that returns a dict simple struct for json serializtion of object"""


def class_to_json(obj):
    return obj.__dict__
