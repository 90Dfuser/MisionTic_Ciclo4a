class Result_controller:
    def __init__(self):
        print("Table controller ready....")

    def index(self) -> list:
        print("Get all")

    def show(self, id_: str) -> dict:
        print("Show by id")

    def create(self, result_: dict) -> dict:
        print("Insert")

    def update(self, id_: str, result_: dict) -> dict:
        print("Update")

    def delete(self, id_: str) -> str:
        print("Delete")


