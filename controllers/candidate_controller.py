from models.candidates import Candidate
from repositories.candidate_repository import CandidateRepository

class CandidateController:
    def __init__(self):
        print("|Ready| Candidate controller")
        self.candidate_repository = CandidateRepository()

    def index(self) -> list:
        return self.candidate_repository.find_all()

    def show(self, id_: str) -> dict:
        return self.candidate_repository.find_by_id(id_)

    def create(self, candidate_: dict) -> dict:
        candidate = Candidate(candidate_)
        return self.candidate_repository.save(candidate)

    def update(self, id_, candidate_: dict) -> dict:
        candidate = Candidate(candidate_)
        return self.candidate_repository.update(id_, candidate)

    def delete(self, id_: str) -> str:
        return self.candidate_repository.delete(id_)