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

    def all(self, cls=None):
        """Returns the dictionary object"""

        if not cls:
            return self.__objects

        return {key: obj
                for key, obj in self.__objects.items()
                if type(obj) == cls}

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

    def delete(self, obj=None):
        """Deletes `obj` from `objects` dictionary

        Arguments:
            obj (instance): instance of a class to delete
        """
        from models.base_model import BaseModel

        if not obj:
            return

        if not isinstance(obj, BaseModel):
            raise TypeError(f"{obj} must be an instance of BaseModel")

        try:
            key = f"{obj.__class__.__name__}.{obj.id}"
            del FileStorage.__objects[key]
            FileStorage.save(self)
        except KeyError:
            pass

    def close(self):
        """Calls reload method to serialize JSON objects"""
        self.reload()

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

    def get(self, cls, id):
        """Gets an object of type `cls` with given `id` in file storage"""
        if cls not in self.classes and cls not in self.classes.values():
            raise TypeError("{} is not a valid class".format(cls))

        if type(id) != str:
            raise TypeError("{} must be a string".format(id))

        if type(cls) == str:
            cls = self.classes[cls]

        return next((obj for obj in self.all(cls).values() if obj.id == id),
                    None)
