from application.domain.grafos import GrafosDomain
from application.repositories.grafos import GrafosRepositories
from flask import jsonify

class GrafosControllerPost:
    
    @staticmethod
    def Create(name, friends):
        newPerson = {name: friends}
        data = GrafosRepositories.LoadGrafosDataframe()
        if GrafosDomain.NameInNodes(data, name):
            err = {
                "err": f"name {name} already exists"
            }
            return err, 400
        if GrafosDomain.FriendsValidationExist(data, friends):
            err = {
                "err": f"friend name dont exists"
            }
            return err, 400
        GrafosRepositories.AddNewPerson(newPerson)
        return jsonify({"newPerson": newPerson}) , 200