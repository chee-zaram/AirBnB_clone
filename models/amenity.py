#!/usr/bin/python3
"""This is the `amenity` module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Inherits from the `BaseModel` class

    Attributes:
        name (str): Name of the amenity
    """

    name = ""
