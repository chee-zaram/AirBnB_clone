#!/usr/bin/python3
"""This is the `place` module"""

from models.base_model import BaseModel


class Place(BaseModel):
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

    city_id = user_id = name = description = ""
    number_rooms = number_bathrooms = max_guest = price_by_night = 0
    latitude = longitude = 0.0
    amenity_ids = []
