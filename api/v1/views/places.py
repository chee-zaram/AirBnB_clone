#!/usr/bin/python3
"""This view implements the RESTful API operations for `Place` objects"""
from flask import jsonify, abort, request, make_response
from . import app_views
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity


@app_views.route('/cities/<city_id>/places', methods=['GET'])
def read_places(city_id):
    """Retrieves the list of all `Place` objects of a city"""

    if storage.get(City, city_id) is None:
        abort(404)

    places = storage.all(Place).values()
    return jsonify([
        place.to_dict() for place in places if place.city_id == city_id
    ])


@app_views.route('/places/<place_id>', methods=['GET'])
def read_place(place_id):
    """Retrieves the `Place` object with the given `place_id`"""

    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """Deletes the `Place` object with the given `place_id`"""

    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    storage.delete(place)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/places', methods=['POST'])
def create_place(city_id):
    """Creates a new `Place` object associated with the given `city_id`"""
    if storage.get(City, city_id) is None:
        abort(404)

    place_data = request.get_json(silent=True)
    if place_data is None:
        abort(400, "Not a JSON")
    if "user_id" not in place_data:
        abort(400, "Missing user_id")

    user_id = place_data["user_id"]
    if storage.get(User, user_id) is None:
        abort(404)

    if "name" not in place_data:
        abort(400, "Missing name")

    place_data["city_id"] = city_id
    allowed = (
        "city_id", "user_id", "name", "description", "number_rooms",
        "number_bathrooms", "max_guest", "price_by_night",
    )

    new_place = Place()
    for key, value in place_data.items():
        if key in allowed:
            setattr(new_place, key, value)

    new_place.save()
    return make_response(jsonify(new_place.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    """Updates the `Place` object with the given `place_id`"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    place_data = request.get_json(silent=True)
    if place_data is None:
        abort(400, "Not a JSON")

    allowed = (
        "name", "description", "number_rooms", "number_bathrooms",
        "max_guest", "price_by_night",
    )

    for key, value in place_data.items():
        if key in allowed:
            setattr(place, key, value)

    place.save()
    return make_response(jsonify(place.to_dict()), 200)


@app_views.route('/places_search', methods=['POST'])
def search_places():
    """Search for places based on a given request"""

    request_data = request.get_json(silent=True)
    if request_data is None:
        abort(400, "Not a JSON")

    allowed = ("states", "cities", "amenities")
    places = storage.all(Place).values()
    cities = storage.all(City).values()
    states = storage.all(State).values()

    """ If request_data is empty dict or all its items are empty lists
    """
    if not request_data or all(
            v == [] for k, v in request_data.items() if k in allowed):
        return make_response(jsonify([
            place.to_dict() for place in places
        ]), 200)

    city_ids = request_data.get("cities")
    state_ids = request_data.get("states")
    amenity_ids = request_data.get("amenities")

    # If there are specific cities, get them
    if city_ids:
        rv = [city for city in cities if city.id in city_ids]
    # If not specific cities and states aren't specified
    elif not state_ids:
        rv = [city for city in cities]
        city_ids = [city.id for city in rv]
    else:
        rv = city_ids = []

    if state_ids:
        states = [state for state in states if state.id in state_ids]
        [
            rv.append(city) for state in states for city in state.cities
            if city.id not in city_ids
        ]

        city_ids = [city.id for city in rv]

    if amenity_ids:
        rv = [
            place for place in places
            if place.city_id in city_ids and all(storage.get(
                Amenity, amenity_id) in place.amenities
                for amenity_id in amenity_ids)
        ]
    else:
        rv = [place for place in places if place.city_id in city_ids]

    reval = []
    for am in rv:
        """
        If the source is db, there will be an `amenities` attribute which is a
        list of all the `Amenity` objects, and they are not JSON serializable
        so we remove the list
        """
        d = am.to_dict()
        d.pop("amenities", None)
        reval.append(d)

    return make_response(jsonify(reval), 200)
