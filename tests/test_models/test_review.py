#!/usr/bin/python3
"""Test module tests the ``Review`` class, using unittesting"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.review import Review


class TestBase(unittest.TestCase):
    """Test class for unittests.
    It inherits from unittest's ``TestCase``

    A ``Review`` instance will hereafter
    be simply referred to as an "instance"
    """

    def test_instance(self):
        """Checks that an instance is created properly"""
        p1 = Review()
        p2 = Review()
        self.assertTrue(isinstance(p1, Review))
        self.assertTrue(isinstance(p2, Review))
        self.assertTrue(type(p1) == Review)
        self.assertFalse(type(p2) != Review)
        self.assertFalse(isinstance(p1, int))
        self.assertFalse(isinstance(p2, list))
        self.assertFalse(p1 is p2)

    def test_inheritance(self):
        """Checks that an instance inherits from the ``BaseModel`` class"""
        p1 = Review()
        p2 = Review()
        self.assertTrue(isinstance(p1, BaseModel))
        self.assertTrue(isinstance(p2, BaseModel))
        self.assertFalse(isinstance(p1, int))
        self.assertFalse(isinstance(p2, list))
        self.assertEqual(len(p2.id), 36)
        self.assertFalse(type(p2) == BaseModel)
        self.assertFalse(type(p1) == BaseModel)
        self.assertTrue(type(p1.created_at) == datetime)
        self.assertTrue(type(p2.updated_at) == datetime)

    def test_attributes(self):
        """Checks that an instance has the correct and complete attributes"""
        p1 = Review()
        p2 = Review()
        a_attr = getattr(p1, "place_id")
        self.assertTrue(a_attr == "")
        p1.place_id = "Ba-123"
        self.assertEqual(p1.place_id, "Ba-123")
        self.assertTrue(type(p1.place_id) == str)

        a_attr = getattr(p1, "user_id")
        self.assertTrue(a_attr == "")
        p1.user_id = "987"
        self.assertEqual(p1.user_id, "987")
        self.assertTrue(type(p1.user_id) == str)

        a_attr = getattr(p1, "text")
        self.assertTrue(a_attr == "")
        p1.text = "Amazing place, good food"
        self.assertEqual(p1.text, "Amazing place, good food")
        self.assertTrue(type(p1.text) == str)

        self.assertTrue(p2.id)
        self.assertEqual(len(p1.id), 36)
        self.assertFalse(p1.id == p2.id)

        self.assertTrue(p1.created_at)
        self.assertTrue(type(p1.created_at) == datetime)
        self.assertFalse(p1.created_at == p2.created_at)

        self.assertTrue(p1.updated_at)
        self.assertTrue(type(p1.updated_at) == datetime)
        self.assertFalse(p1.updated_at == p2.updated_at)

        self.assertTrue(p2.place_id == "")
        self.assertFalse(p1.place_id == "")
        self.assertTrue(p2.user_id == "")
        self.assertFalse(p1.user_id == "")
        self.assertTrue(p2.text == "")
        self.assertFalse(p1.text == "")

        a_attr = getattr(p2, "__class__")
        self.assertFalse(a_attr == 'Place')
        self.assertNotEqual(a_attr, "Place")


if __name__ == "__main__":
    unittest.main()
