#!/usr/bin/python3
"""Test module tests the ``Amenity`` class, using unittesting"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test class for unittests.
    It inherits from unittest's ``TestCase``

    An ``Amenity`` instance will hereafter
    be simply referred to as an "instance"
    """

    def test_instance(self):
        """Checks that an instance is created properly"""
        a1 = Amenity()
        a2 = Amenity()
        self.assertTrue(isinstance(a1, Amenity))
        self.assertTrue(isinstance(a2, Amenity))
        self.assertTrue(type(a1) == Amenity)
        self.assertFalse(type(a2) != Amenity)
        self.assertFalse(isinstance(a1, int))
        self.assertFalse(isinstance(a2, list))
        self.assertFalse(a1 is a2)

    def test_inheritance(self):
        """Checks that an instance inherits from the ``BaseModel`` class"""
        a1 = Amenity()
        a2 = Amenity()
        self.assertTrue(isinstance(a1, BaseModel))
        self.assertTrue(isinstance(a2, BaseModel))
        self.assertFalse(isinstance(a1, int))
        self.assertFalse(isinstance(a2, list))
        self.assertEqual(len(a2.id), 36)
        self.assertFalse(type(a2) == BaseModel)
        self.assertFalse(type(a1) == BaseModel)
        self.assertTrue(type(a1.created_at) == datetime)
        self.assertTrue(type(a2.updated_at) == datetime)

    def test_attributes(self):
        """Checks that an instance has the correct and complete attributes"""
        a1 = Amenity()
        a2 = Amenity()
        a_attr = getattr(a1, "name")
        self.assertTrue(a_attr == "")
        a1.name = "Chee-z"
        self.assertEqual(a1.name, "Chee-z")
        self.assertTrue(type(a2.name) == str)

        self.assertTrue(a2.id)
        self.assertEqual(len(a1.id), 36)
        self.assertTrue(a1.id != a2.id)

        self.assertTrue(a1.created_at)
        self.assertTrue(type(a1.created_at) == datetime)
        self.assertTrue(a1.created_at != a2.created_at)

        self.assertTrue(a1.updated_at)
        self.assertTrue(type(a1.updated_at) == datetime)
        self.assertTrue(a1.updated_at != a2.updated_at)


if __name__ == "__main__":
    unittest.main()
