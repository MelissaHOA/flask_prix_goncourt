import sqlite3
from models.livre import Livre
from typing import List

class LivresDAO:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def get_all_livres(self) -> List[Livre]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM le_prix_goncourt_livres"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Livre(*row) for row in rows]

    def get_livres_by_selection(self, selection_date: str) -> List[Livre]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = """
                SELECT l.id_livre, l.titre, l.auteur, l.resume_livre, l.prix
                FROM le_prix_goncourt_livres l
                JOIN le_prix_goncourt_selectionner s ON l.id_livre = s.id_livre
                WHERE s.date_selection = ?
            """
            cursor.execute(query, (selection_date,))
            rows = cursor.fetchall()
            return [Livre(*row) for row in rows]
