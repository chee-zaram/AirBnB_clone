#!/usr/bin/python3
"""This is the `review` module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import storage_type


class Review(BaseModel, Base):
    """This class inherits from `BaseModel`

    Attributes:
        place_id (str): This stores the <Place.id>
        user_id (str): This stores the <User.id>
        text (str): This is the review text
    """

    if storage_type == "db":
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey(
            "places.id", ondelete='CASCADE', onupdate='CASCADE'),
            nullable=False)
        user_id = Column(String(60), ForeignKey(
            "users.id", ondelete='CASCADE', onupdate='CASCADE'),
            nullable=False)
        text = Column(String(1024), nullable=False)

    else:
        place_id = user_id = text = ""
