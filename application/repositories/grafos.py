import json
import pandas as pd

class GrafosRepositories:

    def LoadGrafos():
        data = open("grafos.json")
        data = json.load(data)
        return pd.DataFrame.from_dict(data, orient='index').transpose()
