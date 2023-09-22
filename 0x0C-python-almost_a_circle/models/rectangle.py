#!/usr/bin/python3
"""
This module contains a Rectangle class
that inherits from the Base class
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        setter function for width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter function for width

        Args:
            value (int): value of the width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        setter function for height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        setter function for height

        Args:
            value (int): value of the width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        setter function for x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        setter function for x

        Args:
            value (int): value of x

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        setter function for y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        setter function for y

        Args:
            value (int): value of y

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Computes area for rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """ function display """
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for a in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return f"[Rectangle] ({self.__id}) {self.__x}/{self.__y}
    - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        If args: set attributes in this order: id, width, height, x, y
        If no args given: set attributes according to kwargs
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.width = v
                elif k == 2:
                    self.height = v
                elif k == 3:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
