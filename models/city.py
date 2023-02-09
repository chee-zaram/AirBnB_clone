#!/usr/bin/python3
"""This is the `city` module"""

from models.base_model import BaseModel


class City(BaseModel):
    """Inherits from `BaseModel` class

    Attributes:
        state_id (str): Stores the <State.id>
        name (str): Name of the city
    """

    state_id = ""
    name = ""
