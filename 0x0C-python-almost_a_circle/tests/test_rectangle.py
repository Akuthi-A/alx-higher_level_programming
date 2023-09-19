#!/usr/bin/python3
"""
Tests attributes & methods of the rectangle class
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    Test class for Rectangle
    """

    def test_inheritance(self):
        """
        tests for inheritance
        """
        self.obj = Rectangle(2, 3)
        self.assertTrue(isinstance(self.obj, Rectangle))
        self.assertTrue(isinstance(self.obj, Base))
        self.assertTrue(isinstance(Rectangle, Base))

    def test_init(self):
        """
        tests init function
        """
        self.obj = Rectangle(2, 3, 4, 5)
        self.assertEqual(self.obj.width, 2)
        self.assertEqual(self.obj.height, 3)
        self.assertEqual(self.obj.x, 4)
        self.assertEqual(self.obj.y, 5)

        self.obj = Rectangle(2, 3)
        self.assertEqual(self.obj.x, 0)
        self.assertEqual(self.obj.y, 0)

    def test_raises(self):
        """
        tests if errors are being raised
        """
        with self.assertRaises(ValueError):
            self.obj = Rectangle(0, 5)
        with self.assertRaises(ValueError):
            self.obj = Rectangle(5, 0)
        with self.assertRaises(TypeError):
            self.obj = Rectangle(5, "five")
        with self.assertRaises(TypeError):
            self.obj = Rectangle("five", 5)
        with self.assertRaises(ValueError):
            self.obj = Rectangle(5, 4, 3, 0)

    def test_area(self):
        """
        Tests for the area of the rectangle
        """
        self.obj = Rectangle(4, 5)
        self.assertEqual(self.obj.area(), 20)
        self.obj = Rectangle(5, 5, 0, 0)
        self.assertEqual(self.obj.area(), 25)
