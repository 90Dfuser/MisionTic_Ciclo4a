from models.tables import Table
class TableController:
    def __init__(self):
        print("Table controller |Ready|")

    def index(self) -> list:
        print("Get all")
        votos_totales = 99
        data = {
            "id": "abc123",
            "cantidad_votos": votos_totales,
            "candidato_1": 50,
            "candidato_2": 49
        }
        return [data]

    def show(self, id_: str) -> dict:
        print("Show by id")
        data = {
            "_id": id_,
            "cantidad_inscritos": "3"
        }
        return data

    def create(self, table_: dict) -> dict:
        print("Insert")
        table = Table(table_)
        return table.__dict__

    def update(self, id_: str, table_: dict) -> dict:
        print("Update")
        data = table_
        data["id"] = id_
        table = Table(table_)
        return table.__dict__

    def delete(self, id_: str) -> str:
        print("Delete: " + id_)
        return {"delete-cont": 8}

