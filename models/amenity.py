#!/usr/bin/python3
"""This is the `amenity` module"""

from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Inherits from the `BaseModel` class

    Attributes:
        name (str): Name of the amenity
    """

    if storage_type == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""
