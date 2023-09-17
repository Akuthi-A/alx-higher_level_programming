#!/usr/bin/python3
"""
This module defines a class `Rectangle`
that inherits from `BaseGeometry`
"""


class BaseGeometry:
    """
    Blueprint for BaseGeometry
    """

    def area(self):
        """
        function that's supposed to implement computation of area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates if the entered value is an integer

        Args:
            name (str): name of value
            value (int): value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Blueprint for Rectangle

    Args:
        BaseGeometry (class): class inherited from (parent class)
    """

    def __init__(self, width, height):
        """
        init method
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Implementation of area of a rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """
    Blueprint for a Square
    """

    def __init__(self, size):
        """
        Initializer function for Square class
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__width}/{self.__height}"
