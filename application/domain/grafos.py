import pandas as pd

class GrafosDomain:

    def NameInNodes(data, name):
        if name in data.columns.to_list():
            return True
        else:
            False
