#!/usr/bin/python3
"""This is the `state` module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import storage_type
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Inherits from `BaseModel`

    Attributes:
        name (str): Name of the State
    """

    __tablename__ = "states"
    if storage_type == "db":
        name = Column(String(60), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")

    else:
        name = ""

        @property
        def cities(self):
            """Returns a list of cities in the state for file storage engine"""
            from models.city import City
            from models import storage

            cities = storage.all(City).values()
            return [city for city in cities if city.state_id == self.id]
