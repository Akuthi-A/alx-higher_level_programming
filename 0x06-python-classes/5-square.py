#!/usr/bin/python3

"""
square class
"""


class Square:
    """blueprint of a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """
        getter function for size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setter function for size

        Args:
            value (int): input size
        Raises:
            TypeError: if size is not an int
            ValueError: if size < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
