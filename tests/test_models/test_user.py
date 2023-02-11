#!/usr/bin/python3
"""This module contains unittest for `User` class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """This class inherits from `unittest.TestCase` and defines a set of test
    cases for the `User` class
    """

    def setUp(self):
        """Runs before every test method"""
        self.user = User()
        self.user.email = "user@email.com"
        self.user.password = "password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

    def test_attributes(self):
        """Test attributes"""
        self.assertEqual(self.user.email, "user@email.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_attributes_types(self):
        """Test attribute types"""
        self.assertTrue(str, self.user.email)
        self.assertTrue(str, self.user.password)
        self.assertTrue(str, self.user.first_name)
        self.assertTrue(str, self.user.last_name)

    def test_save(self):
        """Test the `save` method"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """Test the `to_dict` method"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["email"], "user@email.com")
        self.assertEqual(user_dict["password"], "password")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")

    def test_inheritance(self):
        """Tests for inheritance"""
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(type(self.user) is User)
        self.assertFalse(type(self.user) is BaseModel)


if __name__ == "__main__":
    unittest.main()
