from dao.livres_dao import LivresDAO

class SelectionService:
    def __init__(self, livres_dao: LivresDAO):
        self.livres_dao = livres_dao

    def get_livres_premiere_selection(self):
        return self.livres_dao.get_livres_by_selection("2024-09-03")

    def get_livres_deuxieme_selection(self):
        return self.livres_dao.get_livres_by_selection("2024-10-01")

    def get_livres_troisieme_selection(self):
        return self.livres_dao.get_livres_by_selection("2024-10-22")
