#!/usr/bin/python3
""" unittest for class Base."""


import unittest
import inspect
import json
from models import base
from models.base import Base


class TestBaseDocstrings(unittest.TestCase):
    """ The unittest class for the Base class """

    @classmethod
    def setUpClass(cls):
        """ setting up the class for our doctests."""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_module_doc(self):
        """Testing function documentation"""

        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """ Testing class documentation"""

        self.assertTrue(len(Base.__doc__) > 0)

    def test_instance_id(self):
        """Test the process of id generation"""

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_func_docstrings(self):
        """Testing whether all functions have docstrings"""
        for func in self.base_funcs:
            self.assertTrue(len([1].__doc__) > 0)

    class TestBase(unittest.TestCase):
        """ checking the functionality of class Base"""
        def test_extra_args(self):
            """ tests for extra args to init class constructor."""
            with self.assertRaises(TypeError):
                b = Base(1, 1)

        def test_no_id(self):
            """ tests to check whether the id has been passed"""
            b = base()
            self.assertEqual(b.id, 1)

        def test_id_specified(self):
            """tests when another id (other than None) is passed"""
            b97 = Base(97)
            self.assertEqual(b97.id, 97)

        def test_no_id_after_setting(self):
            """ Test whether the new id is none after already passing None"""
            b2 = Base()
            self.assertEqual(b2.id, 2)

        def test_nb_private(self):
            """ tests nb_objects as private instance attributes."""
            b = Base(3)
            with self.assertRaises(AttributeError):
                print(b.nb_objects)
            with self.assertRaises(AttributeError):
                print(b.__nb_objects)

        def test_to_json_string(self):
            """Tests conversion of python objects to json strings"""
            Base._Base__nb_objects = 0
            dict1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
            dict2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
            json_str = Base.to_json_string([dict1, dict2])
            self.assertTrue(type(json_str) is str)
            d = json.loads(json_str)
            self.assertEqual(d, [dict1, dict2])

        def test_empty_to_json_string(self):
            """ test for empty lists passed"""
            json_str = Base.to_json_string([])
            self.assertTrue(type(json_str) is str)
            self.assertEqual(json_str, "[]")

        def test_None_to_json_string(self):
            """checking for None"""
            json_str = Base.to_json_string(None)
            self.assertTrue(type(json_str) is str)
            self.assertEqual(json_str, "[]")

        def test_from_json_string(self):
            """ tests for conversion of json strings to python objects"""
            json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
                {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
            json_list = Base.from_json_string(json_str)
            self.assertTrue(type(json_list) is list)
            self.assertEqual(len(json_list), 2)
            self.assertTrue(type(json_list[0]) is dict)
            self.assertTrue(type(json_list[1]) is dict)
            self.assertEqual(json_list[0], {
                "id": 9,
                "width": 5,
                "height": 6,
                "x": 7,
                "y": 8
                })
            self.assertEqual(json_list[1], {
                "id": 2,
                "width": 2,
                "height": 3,
                "x": 4,
                "y": 0
                })

        def test_from_json_string_empty(self):
            """tests whether a converted json string is empty"""
            self.assertEqual([], Base.from_json_string(""))

        def test_from_json_string_None(self):
            """"empty string"""
            self.assertEqual([], Base.from_json_string(None))

if __name__ == "__main__":
    unittest.main()
