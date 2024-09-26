from dao.selection_dao import SelectionDAO

class VoteService:
    def __init__(self, selection_dao: SelectionDAO):
        self.selection_dao = selection_dao

    def get_votes_for_livre(self, id_livre: int) -> int:
        return self.selection_dao.get_votes_by_livre(id_livre)
