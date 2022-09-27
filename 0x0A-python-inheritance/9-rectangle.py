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

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """representantion of print() and str()"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
