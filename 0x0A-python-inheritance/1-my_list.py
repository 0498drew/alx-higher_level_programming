#!/usr/bin/python3
"""defines an inheretance class"""


class MyList(list):

    def print_sorted(self):
        """print in sorted order"""
        print(sorted(self))
