#!/usr/bin/python3
"""Defining a function to inserta line to a text"""



def append_after(filename="", search_string="", new_string=""):
    """Insering a line of text to a file

    args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
