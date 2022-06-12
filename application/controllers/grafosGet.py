from application.repositories.grafos import GrafosRepositories


class GrafosControllerGet:
    
    @staticmethod
    def GetAll():
        data = GrafosRepositories.LoadGrafos()
        return data.columns.tolist()

    @staticmethod
    def GetByID(level, id):
        return level, id