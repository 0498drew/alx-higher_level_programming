#!/usr/bin/python3
"""Defining a class of a square"""
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """Intialazing square attributes

        args:
            id : indentation of the square
            x: X cordinates of the square
            y: Y cordinates of the square
            width: width of the square
            height: height of the square
        """
        super().__init__(size, size, y, x, id)

    @property
    def size(self):
        """get size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """get size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """print() and str() presentention"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args,  **kwargs):
        """Updating the new attributes of square"""
        if agrs and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.y, self.x)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = agr
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v, in kwargs.items:
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x == v
                elif k == "y":
                    self.y == v

    def to_dictionar(self):
        """dictonary of a square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}
