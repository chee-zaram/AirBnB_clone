#!/usr/bin/python3
"""This is the ``base_model`` module

It contains the class `BaseModel`
"""

from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


@dataclass(unsafe_hash=True)
class BaseModel:
    """This is the class `BaseModel`

    It defines all common attributes/methods for other classes
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Runs only once when a new instance is created

        Initializes attributes for every instance of `BaseModel` or sub-classes

        Args:
            args (tuple): List of positional arguments (unused)
            kwargs (dict): Key/Value pairs of attribute names and values
        """

        if kwargs:
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid4())
                kwargs['created_at'] = datetime.now()
                kwargs['updated_at'] = datetime.now()
                self.__dict__.update(kwargs)
            else:
                dict_obj = BaseModel.from_dict(kwargs)
                self.__dict__.update(dict_obj)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Prints out a string representation of the class instance"""

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute `updated_at`

        This attributes is updated with the current datetime
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self, to_save=False):
        """Returns a `dict` of all key/value pairs of the given instance"""

        dict_obj = self.__dict__.copy()
        if "_sa_instance_state" in dict_obj:
            del dict_obj["_sa_instance_state"]
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()

        if not to_save and dict_obj["__class__"] == "User":
            del dict_obj["password"]

        return dict_obj

    def delete(self):
        """Delete instance from storage."""
        from models import storage
        storage.delete(self)

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
