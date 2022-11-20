from models.candidates import Candidate
from models.politicalParties import PoliticalParty
from repositories.candidate_repository import CandidateRepository
from repositories.political_parties_repository import PoliticalPartyRepository


class CandidateController:
    def __init__(self):
        print("|Ready| Candidate controller")
        self.candidate_repository = CandidateRepository()
        self.political_party_repository = PoliticalPartyRepository()

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

    def delete(self, id_: str) -> dict:
        return self.candidate_repository.delete(id_)

    def political_party_assign(self, candidate_id, political_party_id) -> dict:
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        political_party_dict = self.political_party_repository.find_by_id(political_party_id)
        political_party_obj = PoliticalParty(political_party_dict)
        candidate_obj.political_party = political_party_obj
        return self.candidate_repository.save(candidate_obj)