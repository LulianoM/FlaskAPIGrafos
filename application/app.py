from flask import Flask
from flask_cors import CORS
from application.rest import healthcheck


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    config_module = f"application.config.{config_name.capitalize()}Config"
    app.config.from_object(config_module)
    app.register_blueprint(healthcheck.blueprint)
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
    return app

