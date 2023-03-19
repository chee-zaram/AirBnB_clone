#!/usr/bin/python3
"""This is the ``base_model`` module

It contains the class `BaseModel`
"""

from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime
from models import storage


@dataclass(unsafe_hash=True)
class BaseModel:
    """This is the class `BaseModel`

    It defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Runs only once when a new instance is created

        Initializes attributes for every instance of `BaseModel` or sub-classes

        Args:
            args (tuple): List of positional arguments (unused)
            kwargs (dict): Key/Value pairs of attribute names and values
        """

        if kwargs:
            # Here, if an attribute name we are interested is in kwargs, we use
            # the value to set our instance attribute
            # If it is not, we generate the value of our instance attribute

            if 'id' not in kwargs:
                kwargs['id'] = str(uuid4())
                kwargs['created_at'] = datetime.now()
                kwargs['updated_at'] = datetime.now()
                self.__dict__.update(kwargs)
                storage.new(self)
            else:
                dict_obj = BaseModel.from_dict(kwargs)
                self.__dict__.update(dict_obj)
                # for key, value in dict_obj.items():
                #     setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        # super().__init__()

    def __str__(self):
        """Prints out a string representation of the class instance"""

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute `updated_at`

        This attributes is updated with the current datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a `dict` of all key/value pairs of the given instance"""

        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()

        return dict_obj

    @staticmethod
    def from_dict(dict_obj):
        """Converts specific keys in `dict_obj` from `str` to apprioprate obj

        Args:
            dict_obj (dict): Dictionary of attribute names and values
        """

        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        dict_obj.pop("__class__", None)

        dict_obj["created_at"] = datetime.strptime(
            dict_obj["created_at"], date_format)

        dict_obj["updated_at"] = datetime.strptime(
            dict_obj["updated_at"], date_format)

        return dict_obj
