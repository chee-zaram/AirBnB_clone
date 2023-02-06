#!/usr/bin/python3
"""This is the ``base_model`` module

It contains the class `BaseModel`
"""

from uuid import uuid4
from datetime import datetime


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

            date_format = "%Y-%m-%dT%H:%M:%S.%f"

            if kwargs["id"]:
                self.id = kwargs["id"]
            else:
                self.id = str(uuid4())

            if kwargs["created_at"]:
                date_string = kwargs["created_at"]
                self.created_at = datetime.strptime(date_string, date_format)
            else:
                self.created_at = datetime.now()

            if kwargs["updated_at"]:
                date_string = kwargs["updated_at"]
                self.updated_at = datetime.strptime(date_string, date_format)
            else:
                self.updated_at = datetime.now()

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Prints out a string representation of the class instance """

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute `updated_at`

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
