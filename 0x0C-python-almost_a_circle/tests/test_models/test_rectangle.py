#!/usr/bin/python3
"""unit test module for Base class"""

from io import StringIO
import unittest
import sys

from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Base class unittest"""

    def test_wrong_constructor_args(self):
        """test wrong constructor args"""
        self.assertRaises(TypeError, lambda: Rectangle())

    def test_doc(self):
        """test doc"""
        self.assertGreater(len(Rectangle.__doc__), 1)
        self.assertGreater(len(Rectangle.__init__.__doc__), 1)
        self.assertGreater(len(Rectangle.width.__doc__), 1)
        self.assertGreater(len(Rectangle.height.__doc__), 1)
        self.assertGreater(len(Rectangle.x.__doc__), 1)
        self.assertGreater(len(Rectangle.y.__doc__), 1)
        self.assertGreater(len(Rectangle.area.__doc__), 1)
        self.assertGreater(len(Rectangle.display.__doc__), 1)
        self.assertGreater(len(Rectangle.__str__.__doc__), 1)
        self.assertGreater(len(Rectangle.update.__doc__), 1)
        self.assertGreater(len(Rectangle.to_dictionary.__doc__), 1)

    def test_default_values(self):
        """test default values"""
        Base._Base__nb_objects = 0
        r = Rectangle(10, 10)
        r = Rectangle(10, 10)
        r = Rectangle(10, 10)
        self.assertEqual(r.id, 3)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_int_id(self):
        """test int id"""
        Base. _Base__nb_objects = 0
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_subclass_of_base(self):
        """test subclass of base"""
        self.assertEqual(Rectangle.__base__, Base)

    def test_invalid_args_type(self):
        """test invlaid arguments"""
        with self.assertRaises(TypeError) as e1:
            Rectangle("1", 1)

        with self.assertRaises(TypeError) as e2:
            Rectangle(1, "1")

        with self.assertRaises(TypeError) as e3:
            Rectangle(1, 1, "1")

        with self.assertRaises(TypeError) as e4:
            Rectangle(1, 1, 1, "1")

        self.assertEqual(str(e1.exception), "width must be an integer")
        self.assertEqual(str(e2.exception), "height must be an integer")
        self.assertEqual(str(e3.exception), "x must be an integer")
        self.assertEqual(str(e4.exception), "y must be an integer")

    def test_invalid_args_value(self):
        """test invlaid arguments"""
        with self.assertRaises(ValueError) as e1:
            Rectangle(-1, 1)

        with self.assertRaises(ValueError) as e2:
            Rectangle(1, -1)

        with self.assertRaises(ValueError) as e3:
            Rectangle(1, 1, -1)

        with self.assertRaises(ValueError) as e4:
            Rectangle(1, 1, 1, -1)

        self.assertEqual(str(e1.exception), "width must be > 0")
        self.assertEqual(str(e2.exception), "height must be > 0")
        self.assertEqual(str(e3.exception), "x must be >= 0")
        self.assertEqual(str(e4.exception), "y must be >= 0")

    def test_wrong_area_args(self):
        """test wrong area args"""
        r = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_area_method(self):
        """test area method"""
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

    def test_wrong_display_args(self):
        """test wrong display method args"""
        r = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            r.display(1)

    def test_display_method(self):
        """test display method"""
        stdout = StringIO()
        sys.stdout = stdout
        r = Rectangle(3, 2)
        r.display()

        # restore stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(stdout.getvalue(), "###\n###\n")

    def test_display_method_with_x_and_y(self):
        """test display method"""
        stdout = StringIO()
        sys.stdout = stdout
        r = Rectangle(3, 2, 1, 3)
        r.display()

        # restore stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(stdout.getvalue(), "\n\n\n ###\n ###\n")

    def test___str__(self):
        """test __str__ method"""
        r = Rectangle(4, 6, 2, 1, 12)
        expected_value = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r), expected_value)

    def test_update_args(self):
        """test update args"""
        r = Rectangle(1, 2)
        r.update(100, 1, 2, 3, 4)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_kwargs(self):
        """test update kwargs"""
        r = Rectangle(1, 2)
        r.update(width=99)
        r.update(height=100)
        self.assertEqual(r.width, 99)
        self.assertEqual(r.height, 100)

    def test_update_args_kwargs(self):
        """test update args kwargs"""
        r = Rectangle(1, 2)
        r.update(100, id=99)
        self.assertEqual(r.id, 100)

    def test_to_dictionary(self):
        """test to_dictionary"""
        r = Rectangle(1, 2, 1, 2, 99)
        expected_dict = {"x": 1, "y": 2, "id": 99,
                         "height": 2, "width": 1}
        self.assertDictEqual(r.to_dictionary(), expected_dict)
