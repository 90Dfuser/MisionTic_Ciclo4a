from models.results import Result
from repositories.result_repository import ResulRepository


class Result_controller:
    def __init__(self):
        print("|Ready| Result controller")
        self.result_repository = ResulRepository()

    def index(self) -> list:
        return self.result_repository.find_all()

    def show(self, id_: str) -> dict:
        return self.result_repository.find_by_id(id_)

    def create(self, result_: dict) -> dict:
        result = Result(result_)
        return self.result_repository.save(result)

    def update(self, id_: str, result_: dict) -> dict:
        result = Result(result_)
        return self.result_repository.update(id_, result)

    def delete(self, id_: str) -> dict:
        return self.result_repository.delete(id_)


