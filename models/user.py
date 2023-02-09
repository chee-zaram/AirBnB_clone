#!/usr/bin/python3
"""This module defines a ``User`` class
that inherits from the ``BaseModel`` class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines a User based on the ``BaseModel`` class

    Attributes:
        email (str): the user's email
        password (str): the user's password
        first_name (str): the user's first name
        last_name (str): the user's last name
    """

    email = password = first_name = last_name = ""
