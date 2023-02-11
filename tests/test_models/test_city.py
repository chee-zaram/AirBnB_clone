#!/usr/bin/python3
"""Test module tests the ``City`` class, using unittesting"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """Test class for unittests.
    It inherits from unittest's ``TestCase``

    A ``City`` instance will hereafter
    be simply referred to as an "instance"
    """

    def test_instance(self):
        """Checks that an instance is created properly"""
        c1 = City()
        c2 = City()
        self.assertTrue(isinstance(c1, City))
        self.assertTrue(isinstance(c2, City))
        self.assertTrue(type(c1) == City)
        self.assertFalse(type(c2) != City)
        self.assertFalse(isinstance(c1, int))
        self.assertFalse(isinstance(c2, list))
        self.assertFalse(c1 is c2)

    def test_inheritance(self):
        """Checks that an instance inherits from the ``BaseModel`` class"""
        c1 = City()
        c2 = City()
        self.assertTrue(isinstance(c1, BaseModel))
        self.assertTrue(isinstance(c2, BaseModel))
        self.assertFalse(isinstance(c1, int))
        self.assertFalse(isinstance(c2, list))
        self.assertEqual(len(c2.id), 36)
        self.assertFalse(type(c2) == BaseModel)
        self.assertFalse(type(c1) == BaseModel)
        self.assertTrue(type(c1.created_at) == datetime)
        self.assertTrue(type(c2.updated_at) == datetime)

    def test_attributes(self):
        """Checks that an instance has the correct and complete attributes"""
        c1 = City()
        c2 = City()
        a_attr = getattr(c1, "state_id")
        self.assertTrue(a_attr == "")
        c1.state_id = "DXB-19"
        self.assertEqual(c1.state_id, "DXB-19")
        self.assertTrue(type(c1.state_id) == str)

        a_attr = getattr(c1, "name")
        self.assertTrue(a_attr == "")
        c1.name = "Dubai"
        self.assertEqual(c1.name, "Dubai")
        self.assertTrue(type(c1.name) == str)

        self.assertTrue(c2.id)
        self.assertEqual(len(c1.id), 36)
        self.assertTrue(c1.id != c2.id)

        self.assertTrue(c1.created_at)
        self.assertTrue(type(c1.created_at) == datetime)
        self.assertTrue(c1.created_at != c2.created_at)

        self.assertTrue(c1.updated_at)
        self.assertTrue(type(c1.updated_at) == datetime)
        self.assertTrue(c1.updated_at != c2.updated_at)

        self.assertTrue(c1.name != "")
        self.assertTrue(c2.name == "")


if __name__ == "__main__":
    unittest.main()
