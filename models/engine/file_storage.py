#!/usr/bin/python3
"""This is the ``file_storage`` module"""

import json


class FileStorage:
    """This is the `FileStorage` class

    It serializes instances to JSON file, deserializes JSON file to instances
    """

    __file_path = "file_database.json"
    __objects = {}

    def all(self):
        """Returns the dictionary object"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in the dictionary `obj` with key `<obj class name>.id`

        Args:
            obj: An instance of a class
        """

        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """Serializes dictionary of objects to the JSON file"""

        with open(self.__file_path, "w") as file:
            json.dump({key: obj.to_dict()
                      for key, obj in FileStorage.__objects.items()}, file)

    def reload(self):
        """Deserializes the JSON file to dictionary of objects if file exists
        """

        filename = FileStorage.__file_path

        try:
            with open(filename, "r") as file:
                data = json.load(file)
                FileStorage.__objects = {key: self.classes[value["__class__"]](
                    **value) for key, value in data.items()}
        except FileNotFoundError:
            pass

    @property
    def classes(self):
        """Returns a dictionary with all all valid classes as keys and values
        """
        from models.base_model import BaseModel

        return {"BaseModel": BaseModel}
