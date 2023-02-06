#!/usr/bin/python3
""" This is the ``base_model`` module

It contains the class `BaseModel`
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ This is the class `BaseModel`.

    It defines all common attributes/methods for other classes
    """

    def __init__(self):
        """ Runs only once when a new instance is created

        Initializes attributes for every instance of `BaseModel` or sub-classes
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Prints out a string representation of the class instance """

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute `updated_at`

        This attributes is updated with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a `dict` of all key/value pairs of the given instance """

        instance_dict = self.__dict__
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict
