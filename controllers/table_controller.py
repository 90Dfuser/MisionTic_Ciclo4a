class TableController:
    def __init__(self):
        print("Table controller ready....")

    def index(self) -> list:
        print("Get all")

    def show(self, id_: str) -> dict:
        print("Show by id")

    def create(self,table: dict) -> dict:
        print("Insert")

    def update(self, id_: str, table: dict) -> dict:
        print("Update")

    def delete(self, id_: str) -> str:
        print("Delete")

