import json
import pandas as pd

class GrafosRepositories:

    def LoadGrafos():
        data = open("grafos.json")
        return json.load(data)
    
    def LoadGrafosDataframe():
        data = GrafosRepositories.LoadGrafos()
        return pd.DataFrame.from_dict(data, orient='index').transpose()

    def AddNewPerson(newPerson):
        data =  GrafosRepositories.LoadGrafos()
        data.update(newPerson)
        with open('grafos.json', 'w') as grafosJson:
            json.dump(data, grafosJson)
        return data