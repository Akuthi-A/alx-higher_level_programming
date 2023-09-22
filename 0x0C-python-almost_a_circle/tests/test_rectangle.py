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

def test_display(self):
        """Test method: display"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3).display()
            b = bufr.getvalue()
        self.assertEqual(b, '#####\n#####\n#####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n #####\n #####\n #####\n')

    def test_print(self):
        """Test method: __str__"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (5) 3/4 - 1/2')

    def test_update(self):
        """Test method: update(*args)"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update()
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update(99)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 10/10')
        r.update(99, 1)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/10')
        r.update(99, 1, 2)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/2')
        r.update(99, 1, 2, 3, 4)
        self.assertEqual(str(r), '[Rectangle] (99) 3/4 - 1/2')
        """Test invalid *args"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(99, 1, 2, 3, "string")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(99, 1, 2, 3, -99)
        """Test method: update(*kwargs)"""
        r.update(id=55)
        self.assertEqual(str(r), '[Rectangle] (55) 3/4 - 1/2')
        r.update(id=44, x=770, y=880, width=990)
        self.assertEqual(str(r), '[Rectangle] (44) 770/880 - 990/2')
        """Test mixture of valid and invalid *kwargs"""
        r.update(nokey=1000, invalid=2000, testing=3000, id=4000)
        self.assertEqual(str(r), '[Rectangle] (4000) 770/880 - 990/2')

    def test_to_dictionary(self):
        """Test method: to_dictionary"""
        rdic = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(rdic), dict)
        r2 = Rectangle(10, 10)
        r2.update(**rdic)
        self.assertEqual(str(r2), '[Rectangle] (5) 3/4 - 1/2')
