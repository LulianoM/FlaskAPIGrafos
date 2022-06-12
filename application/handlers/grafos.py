
from flask import Blueprint,jsonify

from application.controllers.grafosGet import GrafosControllerGet

blueprint = Blueprint("grafos", __name__)


@blueprint.route("/grafos", methods=["GET"])
def GetAll():
    value = GrafosControllerGet.GetAll()
    return jsonify({"Nodes": value}) 
    
@blueprint.route("/grafos/<level>/<id>", methods=["GET"])
def GetByID(level, id):
    level_, id_ = GrafosControllerGet.GetByID(level , id)
    return jsonify({"level": level_, "id": id_}), 200

@blueprint.route("/grafos", methods=["POST"])
def Create():
    return jsonify({"grafos post": "ok"}), 200