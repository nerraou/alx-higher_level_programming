#!/usr/bin/python3
"""unit test module for Base class"""

from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """Base class unittest"""

    def test_wrong_constructor_args(self):
        """test wrong constructor args"""
        self.assertRaises(TypeError, lambda: Base(1, 2))

    def test_doc(self):
        """test doc"""
        self.assertGreater(len(Base.__doc__), 1)
        self.assertGreater(len(Base.__init__.__doc__), 1)
        self.assertGreater(len(Base.to_json_string.__doc__), 1)

    def test_none_id(self):
        """test none id"""
        Base._Base__nb_objects = 0
        b = Base()
        b = Base()
        b = Base()
        self.assertEqual(b.id, 3)

    def test_int_id(self):
        """test none id"""
        Base._Base__nb_objects = 0
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_to_json_string_none_arg(self):
        """test to json string with None argument"""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_none_arg(self):
        """test to json string with None argument"""
        json_str = Base.to_json_string([{"x": 1}])
        self.assertEqual(json_str, '[{"x": 1}]')
