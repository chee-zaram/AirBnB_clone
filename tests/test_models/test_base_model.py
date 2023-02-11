#!/usr/bin/python3
"""This is the unittest file for `BaseModel` class"""

import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Defines a set of test cases for the `BaseModel` class"""

    def setUp(self):
        """Sets up test cases"""
        self.model = BaseModel()

    def test_init_args(self):
        """Test the constructor of BaseModel with arguments"""

        model = BaseModel(1, 2)
        self.assertEqual(str, type(model.id))
        self.assertEqual(datetime, type(model.created_at))
        self.assertEqual(datetime, type(model.updated_at))

    def test_init_with_kwargs(self):
        """Test the constructor with key word arguments"""

        model_id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        kwargs = {
            "id": model_id,
            "created_at": created_at.isoformat(),
            "updated_at": updated_at.isoformat()
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, model_id)
        self.assertEqual(model.created_at, created_at)
        self.assertEqual(model.updated_at, updated_at)

        kwargs = {"id": "a76d7d92-12c8-4908-b60d-6d9b9c8e6e97",
                  "created_at": "2022-09-12T10:00:00.000000",
                  "updated_at": "2022-09-12T10:30:00.000000"}

        new_instance = BaseModel(**kwargs)
        self.assertIsInstance(new_instance, BaseModel)
        self.assertEqual(new_instance.id, kwargs["id"])
        self.assertIsInstance(new_instance.created_at, datetime)
        self.assertIsInstance(new_instance.updated_at, datetime)
        self.assertEqual(new_instance.created_at.isoformat(),
                         kwargs["created_at"].split(".")[0])
        self.assertEqual(new_instance.updated_at.isoformat(),
                         kwargs["updated_at"].split(".")[0])

    def test_init_without_kwargs(self):
        """Test the constructor without key word arguments or positional ars"""

        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Test the magic `__str__` method"""

        model_str = str(self.model)
        self.assertIn("BaseModel", model_str)
        self.assertIn(self.model.id, model_str)
        self.assertIn(str(self.model.__dict__), model_str)

    def test_save(self):
        """Test the `save` method"""

        updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(updated_at, self.model.updated_at)
        self.assertIsInstance(storage.all(), dict)
        self.assertTrue(type(self.model).__name__ + "." +
                        self.model.id in storage.all().keys())

    def test_to_dict(self):
        """Test the `to_dict` method"""

        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
