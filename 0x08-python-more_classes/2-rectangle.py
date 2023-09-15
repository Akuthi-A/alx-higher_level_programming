#!/usr/bin/python3
"""
This module defines a rectangle class
"""


class Rectangle:
    """
    Blueprint for a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the attributes of the Rectangle class
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter function for width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter function for widt

        Args:
            value (int): value of the width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        getter function for height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        setter function for height

        Args:
            value (int): value for height

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        returns area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        returns perimeter of rectangle
        """

        if (self.__width == 0) or (self.__height == 0):
            return 0

        return ((2 * self.__width) + (2 * self.__height))
