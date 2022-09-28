#!/usr/bin/python3
"""DEfining a function that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """write an object from json file"""
    with open(filename) as f:
        return json.load(filename)
