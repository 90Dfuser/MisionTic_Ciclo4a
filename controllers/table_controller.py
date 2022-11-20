from models.tables import Table
from repositories.tables_repository import TableRepository


class TableController:
    def __init__(self):
        print("|Ready| Table controller")
        self.table_repository = TableRepository()

    def index(self) -> list:
        return self.table_repository.find_all()

    def show(self, id_: str) -> dict:
        return self.table_repository.find_by_id(id_)

    def create(self, table_: dict) -> dict:
        print("Insert")
        table = Table(table_)
        return self.table_repository.save(table)

    def update(self, id_: str, table_: dict) -> dict:
        print("Update")
        data = table_
        data["id"] = id_
        table = Table(table_)
        return self.table_repository.update(id_, table)

    def delete(self, id_: str) -> dict:
        print("Delete: " + id_)
        return self.table_repository.delete(id_)

