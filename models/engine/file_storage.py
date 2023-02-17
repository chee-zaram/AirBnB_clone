#!/usr/bin/python3
"""This is the ``file_storage`` module"""

import json
from os import path


class FileStorage:
    """This is the `FileStorage` class

    It serializes instances to JSON file, deserializes JSON file to instances
    """

    __file_path = path.join(path.dirname(
        path.realpath(__file__)), "file_database.json")
    __objects = {}

    def all(self):
        """Returns the dictionary object"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in the dictionary `obj` with key `<obj class name>.id`

        Args:
            obj: An instance of a class
        """

        if not obj:
            raise TypeError("Instance cannot be None type")

        if not isinstance(obj, self.classes["BaseModel"]):
            raise TypeError("Object must be an instance of BaseModel")

        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """Serializes dictionary of objects to the JSON file"""

        with open(FileStorage.__file_path, "w") as file:
            json.dump({key: obj.to_dict()
                      for key, obj in FileStorage.__objects.items()},
                      file, indent=2)

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
        """Returns the dictionary of all classes in the program"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        return {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review,
        }
