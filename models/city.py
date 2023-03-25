#!/usr/bin/python3
"""This is the `city` module"""

from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Inherits from `BaseModel` class

    Attributes:
        state_id (str): Stores the <State.id>
        name (str): Name of the city
    """

    __tablename__ = "cities"
    if storage_type == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(60), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete-orphan")
    else:
        state_id = name = ""
