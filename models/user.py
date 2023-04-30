#!/usr/bin/python3
"""This module defines a ``User`` class
that inherits from the ``BaseModel`` class
"""

from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """Defines a User based on the ``BaseModel`` class

    Attributes:
        email (str): the user's email
        password (str): the user's password
        first_name (str): the user's first name
        last_name (str): the user's last name
    """
    __tablename__ = "users"
    if storage_type == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(60), nullable=True)
        last_name = Column(String(60), nullable=True)
        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")
        reviews = relationship("Review", backref="user",
                               cascade="all, delete, delete-orphan")

    else:
        email = password = first_name = last_name = ""

    def __setattr__(self, name, value):
        """Magic method to capture and hash passwords with md5"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super(User, self).__setattr__(name, value)
