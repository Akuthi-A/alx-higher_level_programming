#!/usr/bin/python3
"""
This module defines a rectangle class
"""


class Rectangle:
    """
    Blueprint for a rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes the attributes of the Rectangle class
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

        return ( (2 * self.__width) + (2 * self.__height))

    def __str__(self):
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += str(Rectangle.print_symbol)
            rectangle += "\n"
        return rectangle

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares areas of two rectangles

        Args:
            rect_1 (Rectangle): rectangle 1
            rect_2 (Rectangle): rectangle 2

        Raises:
            TypeError: if args are not instances of Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        returns an instance of Rectangle that is a square (width = height)
        
        Args:
            size (int): size of the sides
        """
        return cls(size, size)
