#!/usr/bin/python3
"""Defining a func that can write a file"""


def write_file(filename="", text=""):
    """Writing a string to text file UTF8.

    Args:
        filename(): the name of the file
        write():  the func to write on a file
    Results:
        returns the number of char written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
