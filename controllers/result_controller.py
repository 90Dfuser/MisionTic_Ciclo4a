from models.candidates import Candidate
from models.results import Result
from models.tables import Table
from repositories.candidate_repository import CandidateRepository
from repositories.result_repository import ResulRepository
from repositories.tables_repository import TableRepository


class Result_controller:
    def __init__(self):
        print("|Ready| Result controller")
        self.result_repository = ResulRepository()
        self.candidate_repository = CandidateRepository()
        self.table_repository = TableRepository()

    def index(self) -> list:
        return self.result_repository.find_all()

    def show(self, id_: str) -> dict:
        return self.result_repository.find_by_id(id_)

    def get_by_candidate(self, candidate_id: str) -> list:
        return self.result_repository.get_candidate_in_result(candidate_id)

    def create(self, result_: dict, candidate_id: str, table_id: str) -> dict:
        result = Result(result_)
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        table_dict = self.table_repository.find_by_id(table_id)
        table_obj = Table(table_dict)
        result.candidate = candidate_obj
        result.table = table_obj
        return self.result_repository.save(result)

    def update(self, id_: str, result_: dict) -> dict:
        result = Result(result_)
        return self.result_repository.update(id_, result)

    def delete(self, id_: str) -> dict:
        return self.result_repository.delete(id_)


