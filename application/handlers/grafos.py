
from flask import Blueprint,jsonify
from application.controllers.grafosGet import GrafosControllerGet

blueprint = Blueprint("grafos", __name__)


@blueprint.route("/grafos", methods=["GET"])
def GetAll():
    return GrafosControllerGet.GetAll()
    
@blueprint.route("/grafos/<level>/<name>", methods=["GET"])
def GetByID(level, name):
    return GrafosControllerGet.GetByID(level , name)

@blueprint.route("/grafos", methods=["POST"])
def Create():
    return jsonify({"grafos post": "ok"}), 200