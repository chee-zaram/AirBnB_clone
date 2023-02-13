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
        file_storage.FileStorage._FileStorage__objects = {}
        self.f_objects = file_storage.FileStorage._FileStorage__objects
        self.base_model = BaseModel()
        self.f_database = os.path.join(os.path.dirname(
            file_storage.__file__), "file_database.json")

    def test_file_path(self):
        """This test case checks the types of all attributes"""

        self.assertEqual(
            self.f_database, file_storage.FileStorage._FileStorage__file_path)
        self.assertTrue(
            type(file_storage.FileStorage._FileStorage__file_path) is str)

    def test_objects(self):
        """Tests case for the objects attributes"""

        self.f_storage.reload()
        self.assertEqual(
            self.f_objects, file_storage.FileStorage._FileStorage__objects)
        self.assertTrue(
            type(file_storage.FileStorage._FileStorage__objects) is dict)

    def test_all(self):
        """Tests the all method"""

        self.f_storage.new(self.base_model)
        objs = self.f_storage.all()
        self.assertEqual(objs, self.f_storage.all())

    def test_new(self):
        """Tests the new method"""

        self.f_storage.new(self.base_model)
        obj = self.f_storage.all()
        key = self.base_model.__class__.__name__ + '.' + self.base_model.id
        self.assertIn(key, obj.keys())
        self.assertEqual(obj[key], self.base_model)

    def test_new_error(self):
        """Test for wrong type in `new` method"""

        with self.assertRaises(TypeError) as e:
            self.f_storage.new("")
        self.assertEqual(
            str(e.exception), "Instance cannot be None type")

        with self.assertRaises(TypeError) as e:
            self.f_storage.new(int)
        self.assertEqual(
            str(e.exception), "Object must be an instance of BaseModel")

    def test_save(self):
        """Tests the save method"""

        self.f_storage.save()
        self.assertTrue(os.path.exists(self.f_database))

    def test_reload(self):
        """Tests the reload method"""

        self.f_storage.save()
        self.f_storage._FileStorage__file_path = {}
        self.f_storage.reload()
        self.assertNotEqual(self.f_storage.all(), {})

    def tearDown(self):
        """Tears down method after test cases"""

        if os.path.exists(self.f_database):
            os.remove(self.f_database)


if __name__ == '__main__':
    unittest.main()
