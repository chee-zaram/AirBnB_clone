#!/usr/bin/python3
"""This is the `review` module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class inherits from `BaseModel`

    Attributes:
        place_id (str): This stores the <Place.id>
        user_id (str): This stores the <User.id>
        text (str): This is the review text
    """

    place_id = user_id = text = ""
