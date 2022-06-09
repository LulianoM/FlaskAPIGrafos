from flask import Blueprint, jsonify


blueprint = Blueprint("healthcheck", __name__)


@blueprint.route("/healthcheck", methods=["GET"])
def index():
    return jsonify({"healthcheck": "ok"}), 200
