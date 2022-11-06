class TableController:
    def __init__(self):
        print("Table controller ready....")

    def index(self) -> list:
        print("Get all")
        data = {
            "id": "abc123",
            "cantidad_inscritos": "3"
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
        table = TableController(table_)
        return table.__dict__

    def update(self, id_: str, table_: dict) -> dict:
        print("Update")
        data = table_
        data["id"] = id_
        table = TableController(table_)
        return table.__dict__

    def delete(self, id_: str) -> str:
        print("Delete" + id_)
        return {"delete-cont": 8}

