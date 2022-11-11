from models.politicalParties import PoliticalParty
from repositories.political_parties_repository import PoliticalPartyRepository


class PoliticalPartyController:
    def __init__(self):
        print("|Ready| Political party controller")
        self.political_party_repository = PoliticalPartyRepository()

    def index(self) -> list:
        return self.political_party_repository.find_all()

    def show(self, id_: str) -> dict:
        return self.political_party_repository.find_by_id(id_)

    def create(self, political_party: dict) -> dict:
        political_party = PoliticalParty(political_party)
        return self.political_party_repository.save(political_party)

    def update(self, id_: str, political_party: dict) -> dict:
        political_party = PoliticalParty(political_party)
        return self.political_party_repository.update(political_party)

    def delete(self, id_: str) -> str:
        return self.political_party_repository.delete(id_)
    # ========================================================================
