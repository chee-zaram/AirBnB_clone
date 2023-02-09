#!/usr/bin/python3
"""This is the `state` module"""

from models.base_model import BaseModel


class State(BaseModel):
    """Inherits from `BaseModel`

    Attributes:
        name (str): Name of the State
    """

    name = ""
