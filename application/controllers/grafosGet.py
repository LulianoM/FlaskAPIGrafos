from application.domain.grafos import GrafosDomain
from application.repositories.grafos import GrafosRepositories

from flask import jsonify


class GrafosControllerGet:
    
    @staticmethod
    def GetAll():
        data = GrafosRepositories.LoadGrafos()
        return jsonify({"Nodes": data.columns.tolist()})  , 200

    @staticmethod
    def GetByID(level, name):
        data = GrafosRepositories.LoadGrafos()
        if GrafosDomain.NameInNodes(data, name):
            return {name: data[name].dropna().tolist()}, 200
        else:
            err = {
                "err": "Name dont exist in nodes"
            }
            return err, 400