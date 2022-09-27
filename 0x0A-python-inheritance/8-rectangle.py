#!/usr/bin/python3
"""defines a rectangle that inherits from basegeomerty"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defining a recatngle"""

    def __init__(self, width, height):
        """intializing a rectangle.

        Args:
            width (int): rectangle width
            height(int): rectangle height
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
