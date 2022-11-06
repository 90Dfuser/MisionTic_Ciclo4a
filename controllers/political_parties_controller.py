class PoliticalPartyController:
    def __init__(self):
        print("Political party controller ready")

    def index(self) -> list:
        print("Get all")

    def show(self, id_: str) -> dict:
        print("Show by id")

    def create(self, political_party: dict) -> dict:
        print("Create")

    def update(self, id_: str, political_party: dict) -> dict:
        print("Update")

    def delete(self, id_: str) -> str:
        print("Delete")
