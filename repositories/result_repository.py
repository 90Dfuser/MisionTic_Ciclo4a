from models.results import Result
from bson import ObjectId
from repositories.interface_repository import InterfaceRepository


class ResulRepository(InterfaceRepository[Result]):
    def get_candidate_in_result(self, candidate_id: str) -> list:
        query = {"candidate.$id": ObjectId(candidate_id)}
        return self.query(query)
