# RESTful API v1.0

This is the first version of the RESTful API for the **AirBnB_clone** project.
The following are endpoints to send requests to the API and requests body should be in JSON format.
If a request is made to one of these endpoints, the corresponding response will be returned in the JSON format.

## Users

- `GET /api/v1/users`: Get all users. Returns a list of dictionaries containing user
  information, with a response code of 200.
- `GET /api/v1/users/<id>`: Get a user with given `id`. Returns a dictionary containing
  user information, with response code of 200.
- `POST /api/v1/users`: Create a new user. Request body must contain `email` and `password`.
  Returns a dictionary containing user information, with response code of 201.
- `PUT /api/v1/users/<id>`: Update a user with given `id`. Request body can only contain
  `first_name`, `last_name`, and `password`. Returns a dictionary containing user's updated information,
  with response code of 200.
- `DELETE /api/v1/users/<id>`: Delete a user with given `id`. Returns an empty dictionary,
  with response code of 200.

## States

- `GET /api/v1/states`: Get all states. Returns a list of dictionaries containing state
  information, with a response code of 200.
- `GET /api/v1/states/<id>`: Get a state with given `id`. Returns a dictionary containing
  state information, with response code of 200.
- `POST /api/v1/states`: Create a new state. Request body must contain `name` of state.
  Returns a dictionary containing state information, with response code of 201.
- `PUT /api/v1/states/<id>`: Update a state with given `id`. Request body can only contain
  `name`. Returns a dictionary containing state's updated information,
  with response code of 200.
- `DELETE /api/v1/states/<id>`: Delete a state with given `id`. Returns an empty dictionary,
  with response code of 200.

## Cities

- `GET /api/v1/cities/<city_id>`: Get a city with `city_id`. Returns a dictionaries containing city information.
- `GET /api/v1/states/<state_id>/cities`: Get a list of all cities associated with a state with given `state_id`.
  Returns a list of dictionaries containing city information, with response code of 200.
- `POST /api/v1/states/<state_id>/cities`: Create a new city associated with state with given `state_id`.
  Request body must contain `name` of city. Returns a dictionary containing city information,
  with response code of 201.
- `PUT /api/v1/cities/<city_id>`: Update a city with given `city_id`.
  Request body can only contain `name` and `state_id`. Returns a dictionary containing city's updated information,
  with response code of 200.
- `DELETE /api/v1/cities/<id>`: Delete a city with given `id`. Returns an empty dictionary,
  with response code of 200.

## Amenities

- `GET /api/v1/amenities`: Get all amenities. Returns a list of dictionaries containing amenities information,
  with a response code of 200.
- `GET /api/v1/amenities/<id>`: Get an amenity with given `id`. Returns a dictionary containing
  amenity information, with response code of 200.
- `POST /api/v1/amenities`: Create a new amenity. Request body must contain `name` of amenity.
  Returns a dictionary containing amenity information, with response code of 201.
- `PUT /api/v1/amenities/<id>`: Update an amenity with given `id`. Request body can only contain
  `name`. Returns a dictionary containing amenity's updated information,
  with response code of 200.
- `DELETE /api/v1/amenities/<id>`: Delete a amenity with given `id`. Returns an empty dictionary,
  with response code of 200.

## Places

- `GET /api/v1/cities/<city_id>/places`: Get all places associated with city with `city_id`.
  Returns a list of dictionaries containing places information, with a response code of 200.
- `GET /api/v1/places/<id>`: Get a place with given `id`. Returns a dictionary containing
  places information, with response code of 200.
- `POST /api/v1/cities/<city_id>/places`: Create a new place associated with city with `city_id`.
  Request body must contain `name` of place and `user_id` of user.
  Returns a dictionary containing place information, with response code of 201.
- `PUT /api/v1/places/<id>`: Update a place with given `id`. Returns a dictionary containing place's updated information,
  with response code of 200.
- `DELETE /api/v1/places/<id>`: Delete a place with given `id`. Returns an empty dictionary,
  with response code of 200.`

## PlacesAmenities

- `GET /api/v1/places/<place_id>/amenities`: Get all amenities associated with place with `place_id`.
  Returns a list of dictionaries containing amenities information, with a response code of 200.
- `POST /api/v1/places/<place_id>/amenities/<amenity_id>`: Create a new association between amenity with given
  `amenity_id` and place with given `place_id`.
  Request body must contain `name` of amenity. Returns a dictionary containing amenity information,
  with response code of 201.
- `PUT /api/v1/places/<place_id>/amenities/<id>`: Update an amenity with given `id`. Returns a dictionary containing
  amenity's updated information, with response code of 200.
- `DELETE /api/v1/places/<place_id>/amenities/<id>`: Delete the association between an amenity with given `id`
  and place with given `place_id`. Returns an empty dictionary, with response code of 200.

## PlacesReviews

- `GET /api/v1/reviews/<id>`: Get a review with given `id`. Returns a dictionary containing review information,
  with response code of 200.
- `GET /api/v1/places/<place_id>/reviews`: Get all reviews associated with place with `place_id`.
  Returns a list of dictionaries containing reviews information, with a response code of 200.
- `POST /api/v1/places/<place_id>/reviews/<review_id>`: Create a new review with given `review_id` and place
  with given `place_id`. Request body must contain `user_id` and `text`.
  Returns a dictionary containing review information, with response code of 201.
- `PUT /api/v1/reviews/<review_id>`: Update a review with given `review_id`. Only `text` field can be updated.
  Returns a dictionary containing review's updated information, with response code of 200.
- `DELETE /api/v1/reviews/<review_id>`: Delete a review with given `review_id`. Returns an empty dictionary,
  with response code of 200.
