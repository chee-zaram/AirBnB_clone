#!/usr/bin/python3
"""Test module tests the ``Place`` class, using unittesting"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.place import Place


class TestBase(unittest.TestCase):
    """Test class for unittests.
    It inherits from unittest's ``TestCase``

    A ``Place`` instance will hereafter
    be simply referred to as an "instance"
    """

    def test_instance(self):
        """Checks that an instance is created properly"""
        p1 = Place()
        p2 = Place()
        self.assertTrue(isinstance(p1, Place))
        self.assertTrue(isinstance(p2, Place))
        self.assertTrue(type(p1) == Place)
        self.assertFalse(type(p2) != Place)
        self.assertFalse(isinstance(p1, int))
        self.assertFalse(isinstance(p2, list))
        self.assertFalse(p1 is p2)

    def test_inheritance(self):
        """Checks that an instance inherits from the ``BaseModel`` class"""
        p1 = Place()
        p2 = Place()
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
        p1 = Place()
        p2 = Place()
        a_attr = getattr(p1, "name")
        self.assertTrue(a_attr == "")
        p1.name = "Bali Towers"
        self.assertEqual(p1.name, "Bali Towers")
        self.assertTrue(type(p1.name) == str)

        a_attr = getattr(p1, "description")
        self.assertTrue(a_attr == "")
        p1.description = "2 bedroom apartment"
        self.assertEqual(p1.description, "2 bedroom apartment")
        self.assertTrue(type(p1.description) == str)

        a_attr = getattr(p1, "city_id")
        self.assertTrue(a_attr == "")
        p1.city_id = "BA-1289"
        self.assertEqual(p1.city_id, "BA-1289")
        self.assertTrue(type(p1.city_id) == str)

        a_attr = getattr(p1, "number_rooms")
        self.assertTrue(a_attr == 0)
        p1.number_rooms = 12
        self.assertEqual(p1.number_rooms, 12)
        self.assertTrue(type(p1.number_rooms) == int)

        a_attr = getattr(p1, "number_bathrooms")
        self.assertTrue(a_attr == 0)
        p1.number_bathrooms = 20
        self.assertEqual(p1.number_bathrooms, 20)
        self.assertTrue(type(p1.number_bathrooms) == int)

        a_attr = getattr(p1, "max_guest")
        self.assertTrue(a_attr == 0)
        p1.max_guest = 50
        self.assertEqual(p1.max_guest, 50)
        self.assertTrue(type(p1.max_guest) == int)

        a_attr = getattr(p1, "price_by_night")
        self.assertTrue(a_attr == 0)
        p1.price_by_night = 6300
        self.assertEqual(p1.price_by_night, 6300)
        self.assertTrue(type(p1.price_by_night) == int)

        a_attr = getattr(p1, "latitude")
        self.assertTrue(a_attr == 0.0)
        p1.latitude = 01.02
        self.assertEqual(p1.latitude, 01.02)
        self.assertTrue(type(p1.latitude) == float)

        a_attr = getattr(p1, "longitude")
        self.assertTrue(a_attr == 0.0)
        p1.longitude = 02.02
        self.assertEqual(p1.longitude, 02.02)
        self.assertTrue(type(p1.longitude) == float)

        a_attr = getattr(p1, "amenity_ids")
        self.assertTrue(a_attr == [])
        p1.amenity_ids = ["BA-1234", "NG-000"]
        self.assertEqual(p1.amenity_ids, ["BA-1234", "NG-000"])
        self.assertTrue(type(p1.amenity_ids) == list)

        self.assertTrue(p2.id)
        self.assertEqual(len(p1.id), 36)

        self.assertTrue(p1.created_at)
        self.assertTrue(type(p1.created_at) == datetime)

        self.assertTrue(p1.updated_at)
        self.assertTrue(type(p1.updated_at) == datetime)

        self.assertTrue(p2.city_id == "")
        self.assertFalse(p1.city_id == "")
        self.assertTrue(p2.user_id == "")
        self.assertTrue(p1.user_id == "")
        self.assertTrue(p2.name == "")
        self.assertFalse(p1.name == "")
        self.assertTrue(p2.description == "")
        self.assertFalse(p1.description == "")
        self.assertTrue(p2.number_rooms == 0)
        self.assertFalse(p1.number_rooms == 0)

        a_attr = getattr(p2, "__class__")
        self.assertFalse(a_attr == 'Place')
        self.assertNotEqual(a_attr, "Place")


if __name__ == "__main__":
    unittest.main()
