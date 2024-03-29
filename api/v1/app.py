#!/usr/bin/python3
""" Root of application """
from os import getenv
from flask import Flask, make_response, jsonify
from .views import app_views
from models import storage
from flask_cors import CORS

# Used to specify host and port for flask to listen on
HBNB_API_HOST = getenv('HBNB_API_HOST', '0.0.0.0')
HBNB_API_PORT = getenv('HBNB_API_PORT', '5000')


def create_app(config_name):
    """Main function"""
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # set up cors
    CORS(app, resources={r"/api/v1/*": {"origins": HBNB_API_HOST}})

    # set configs if available
    if config_name is not None:
        app.config.from_object(config_name)

    # register blueprints
    app.register_blueprint(app_views)

    @app.teardown_appcontext
    def teardown(self):
        """Close the current session"""
        storage.close()

    @app.errorhandler(404)
    def not_found(e):
        """Error handler for the application"""
        return make_response(jsonify({'error': 'Not found'}), 404)

    return app


if __name__ == "__main__":
    """Start of application"""
    app = create_app(None)
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT,
            threaded=True, debug=True, use_evalex=False)
