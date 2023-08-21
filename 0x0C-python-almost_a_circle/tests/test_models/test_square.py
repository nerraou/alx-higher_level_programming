#!/usr/bin/python3
"""unit test module for Base class"""

import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Base class unittest"""

    def test_wrong_constructor_args(self):
        """test wrong constructor args"""
        self.assertRaises(TypeError, lambda: Square())

    def test_doc(self):
        """test doc"""
        self.assertGreater(len(Square.__doc__), 1)
        self.assertGreater(len(Square.__init__.__doc__), 1)
        self.assertGreater(len(Square.__str__.__doc__), 1)
        self.assertGreater(len(Square.update.__doc__), 1)
        self.assertGreater(len(Square.size.__doc__), 1)
        self.assertGreater(len(Square.to_dictionary.__doc__), 1)

    def test_default_values(self):
        """test default values"""
        Base._Base__nb_objects = 0
        s = Square(10, 2)
        s = Square(10, 2)
        s = Square(10, 2)
        self.assertEqual(s.id, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 0)

    def test_subclass_of_base(self):
        """test subclass of base"""
        self.assertEqual(Square.__base__, Rectangle)

    def test___str__(self):
        """test __str__ method"""
        s = Square(4, 2, 1, 12)
        expected_value = "[Square] (12) 2/1 - 4"
        self.assertEqual(str(s), expected_value)

    def test_invalid_size_type(self):
        """test size method"""
        s = Square(4, 2, 1, 12)
        with self.assertRaises(TypeError):
            s.size = "3"

    def test_invalid_size_value(self):
        """test size method"""
        s = Square(4, 2, 1, 12)
        with self.assertRaises(ValueError):
            s.size = -1

    def test_update_args(self):
        """test update args"""
        s = Square(1, 2)
        s.update(100, 1, 3, 4)
        self.assertEqual(s.id, 100)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """test update kwargs"""
        s = Square(1, 2)
        s.update(size=99)
        self.assertEqual(s.size, 99)

    def test_update_args_kwargs(self):
        """test update args kwargs"""
        s = Square(1, 2)
        s.update(100, id=99)
        self.assertEqual(s.id, 100)

    def test_to_dictionary(self):
        """test to_dictionary"""
        s = Square(2, 1, 2, 99)
        expected_dict = {"x": 1, "y": 2, "id": 99,
                         "size": 2}
        self.assertDictEqual(s.to_dictionary(), expected_dict)
