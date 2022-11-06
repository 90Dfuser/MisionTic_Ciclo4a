class ResultController:
    def __init__(self):
        print("Result controller ready...")

    def index(self) -> list:
        print("Get all")

    def show(self, id_: str) -> dict:
        print("Show by id")

    def create(self, result: dict) -> dict:
        print("Insert")

    def update(self, id_: str, result: dict) -> dict:
        print("Update")

    def delete(self, id_: str) -> str:
        print("Delete")
