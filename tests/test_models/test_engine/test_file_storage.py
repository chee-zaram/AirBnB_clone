#!/usr/bin/python3
"""This is a unittest file for the class `file_storage.FileStorage`"""

import unittest
import os
from models.base_model import BaseModel
from models.engine import file_storage


class TestFileStorage(unittest.TestCase):
    """Tests for the file_storage.FileStorage class"""

    def setUp(self):
        """Sets up method for test cases"""

        self.f_storage = file_storage.FileStorage()
        self.f_storage.__objects = {}
        self.base_model = BaseModel()
        self.f_database = os.path.join(os.path.dirname(
            file_storage.__file__), "file_database.json")

    def test_all_method(self):
        """Tests the all method"""

        self.f_storage.new(self.base_model)
        objs = self.f_storage.all()
        self.assertEqual(objs, self.f_storage.all())

    def test_new_method(self):
        """Tests the new method"""

        self.f_storage.new(self.base_model)
        obj = self.f_storage.all()
        key = self.base_model.__class__.__name__ + '.' + self.base_model.id
        self.assertIn(key, obj.keys())
        self.assertEqual(obj[key], self.base_model)

    def test_save_method(self):
        """Tests the save method"""

        self.f_storage.save()
        self.assertTrue(os.path.exists(self.f_database))

    def test_reload_method(self):
        """Tests the reload method"""

        self.f_storage.save()
        self.f_storage.__objects = {}
        self.f_storage.reload()
        self.assertNotEqual(self.f_storage.all(), {})

    def tearDown(self):
        """Tears down method after test cases"""

        if os.path.exists(self.f_database):
            os.remove(self.f_database)


if __name__ == '__main__':
    unittest.main()
