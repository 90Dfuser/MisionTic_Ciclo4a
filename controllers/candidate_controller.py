class CandidateController:
    def __init__(self):
        print("|Ready| Candidate controller")

    def index(self) -> list:
        print("Get all")

    def show(self, id_: str) -> dict:
        print("Show by id")

    def create(self, candidate: dict) -> dict:
        print("Insert")

    def update(self, id_, candidate: dict) -> dict:
        print("Update")

    def delete(self, id_: str) -> str:
        print("Delete")