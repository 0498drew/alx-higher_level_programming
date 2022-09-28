#!/usr/bin/python3
"""Defining a file appended"""


def append_write(filename="", text=""):
    """Append a string at the end of UTF8

    args:
        filename(str): file to be appended to
        txt(str): text to be appended to
    results:
        number of char appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
