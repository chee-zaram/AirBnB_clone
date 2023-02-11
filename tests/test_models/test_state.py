#!/usr/bin/python3
"""This is the unittest module for the `State` class"""

import unittest
from models.state import State
import uuid


class TestState(unittest.TestCase):
    """This is a class that inherits from `unittest.TestCase`"""

    def setUp(self):
        """Runs before each test case"""
        self.model = State()

    def test_attribute_types(self):
        """Tests the types of attributes"""
        self.assertIsInstance(self.model.name, str)

    def test_attribute_values(self):
        """Test the attributes values"""
        self.assertEqual(self.model.name, "")

    def test_save_method(self):
        """Test the save method"""
        pass

    def test_to_dict_method(self):
        """Tests the `to_dict` method"""
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertEqual(sorted(self.model.to_dict().keys()),
                         sorted(expected_keys))

    def test_str_method(self):
        """Tests the `__str__` method"""
        self.assertEqual(str(self.model), "[{}] ({}) {}".format(
            self.model.__class__.__name__, self.model.id, self.model.__dict__))

    def test_args_instantiation(self):
        """Tests the instantiation of arguments"""
        random_uuid = str(uuid.uuid4())
        name = "California"
        kwargs = {
            "id": random_uuid, "name": name,
            "created_at": "2023-02-09T09:09:59.546318",
            "updated_at": "2023-02-09T09:09:59.546318"}

        new_state = State(**kwargs)
        self.assertEqual(new_state.id, random_uuid)
        self.assertEqual(new_state.name, name)


if __name__ == '__main__':
    unittest.main()
