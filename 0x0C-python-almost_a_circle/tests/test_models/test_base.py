#!/usr/bin/python3
"""unit test module for Base class"""

import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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
        self.assertGreater(len(Base.save_to_file.__doc__), 1)
        self.assertGreater(len(Base.from_json_string.__doc__), 1)
        self.assertGreater(len(Base.create.__doc__), 1)
        self.assertGreater(len(Base.load_from_file.__doc__), 1)

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

    def test_save_to_file_none_arg(self):
        """test to json string with None argument"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(None)

        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

    def test_save_to_file_wrong_args_count(self):
        """test to json string with wrong args count"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])

    def test_save_to_file(self):
        """test save to file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        dict1 = r1.to_dictionary()
        dict2 = r2.to_dictionary()
        expected_value = Base.to_json_string([dict1, dict2])

        with open("Rectangle.json", "r") as file:
            value = file.read()
            self.assertEqual(value, expected_value)

        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

    def test_from_json_string_with_args(self):
        """from json string with args"""
        with self.assertRaises(TypeError):
            Base.from_json_string(1, 2)

    def test_from_json_string_no_string_arg(self):
        """from json string with args with no string arg"""
        with self.assertRaises(TypeError):
            Base.from_json_string([1])

    def test_from_json_string(self):
        """from json string with args"""
        list_objs = Base.from_json_string('[{"x": 1}]')
        for obj in list_objs:
            self.assertDictEqual(obj, {"x": 1})

    def test_create_square(self):
        """test create square"""
        s = Square.create(size=99, x=9, y=1)
        self.assertEqual(s.size, 99)
        self.assertEqual(s.x, 9)
        self.assertEqual(s.y, 1)

    def test_create_rectangle(self):
        """test create rectangle"""
        r = Rectangle.create(width=99, height=100, x=9, y=1)
        self.assertEqual(r.width, 99)
        self.assertEqual(r.height, 100)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 1)

    def test_load_from_file_with_args(self):
        """test load from file with args"""
        with self.assertRaises(TypeError):
            Rectangle.load_from_file(1)

    def test_load_from_file(self):
        """test load from file"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        rects_ref = [r1, r2]
        Rectangle.save_to_file(rects_ref)
        rects = Rectangle.load_from_file()

        for i in range(0, len(rects_ref)):
            dict_ref = rects_ref[i].to_dictionary()
            dict = rects[i].to_dictionary()
            self.assertDictEqual(dict_ref, dict)

        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

    def test_load_from_file_file_not_found(self):
        """test load from file"""
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 0)
