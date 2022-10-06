#!/usr/bin/python3
"""Defining a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting fom Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """intializing attributes.

        agrs:
            width: the wew width of a rectangle
            height: the new height of a rectangle
            x: x cordinates of a rectangle
            y: y cordinates of a rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get y cordinates of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y condinates of rectangle"""
        return self.__y

    @x.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Print stdout with chracters #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print() for y in range(0, self.y)]
        for h in range(0, self.height):
            [print(" ", end="") for x in range(0, self.x)]
            [print("#", end="") for w in range(0, self.width)]
            print("")

    def __str__(self):
        """representation of str() and prt() of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Update rectangle attributes

        agrs:
            args(int): new attributes value
            1st attribute representaing id
            2rd attribute representing width
            3rd attribute representing height
            4th attribute representing y
            5th attribute repesenting x
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "v":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictonary(self):
        """Representation of rectangle dict"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}
