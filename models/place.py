#!/usr/bin/python3
"""This is the `place` module"""

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from models import storage_type
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey

if storage_type == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id',
                                            ondelete='CASCADE',
                                            onupdate='CASCADE'),
                                 nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id',
                                            ondelete='CASCADE',
                                            onupdate='CASCADE'),
                                 nullable=False))


class Place(BaseModel, Base):
    """This class inherits from `BaseModel` class

    Attributes:
        city_id (str): This is the <City_id>
        user_id (str): This is the <User.id>
        name (str): This is the name of the place
        description (str): Description of the place
        number_rooms (int): This is the number of rooms
        number_bathrooms (int): This is the numeber of bathrooms in the place
        max_guest (int): This is the maximum number of guest expected
        price_by_night (int): This is the price per night of the place
        latitude (float): This is the latitude of the place
        longitude (float): This is the longitude of the place
        amenity_ids (list): List of strings of <Amenity.id>
    """

    __tablename__ = "places"
    if storage_type == "db":
        city_id = Column(String(60), ForeignKey(
            'cities.id', ondelete='CASCADE'), nullable=False)
        user_id = Column(String(60), ForeignKey(
            'users.id', ondelete='CASCADE'), nullable=False)
        name = Column(String(60), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", backref="place_amenities",
                                 secondary=place_amenity, viewonly=False)

    else:
        city_id = user_id = name = description = ""
        number_rooms = number_bathrooms = max_guest = price_by_night = 0
        latitude = longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """Gets a list of all amenities associated with a place"""
            from models import storage

            return [amenity for amenity in storage.all(Amenity).values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Adds new ids to the list of amenities for a place"""
            if type(obj) != Amenity:
                raise TypeError("Amenity must be an Amenity object")

            if obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
                setattr(self, "amenity_ids", self.amenity_ids)

        @property
        def reviews(self):
            """Gets a list of all reviews associated with a place"""
            from models import storage

            return [review for review in storage.all(Review).values()
                    if review.place_id == self.id]
