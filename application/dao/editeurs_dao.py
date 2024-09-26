import sqlite3
from models.editeur import Editeur
from typing import List

class EditeursDAO:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def get_all_editeurs(self) -> List[Editeur]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM le_prix_goncourt_editeurs"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Editeur(*row) for row in rows]

    def get_editeur_by_id(self, id_editeur: int) -> Editeur:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM le_prix_goncourt_editeurs WHERE id_editeur = ?"
            cursor.execute(query, (id_editeur,))
            row = cursor.fetchone()
            return Editeur(*row) if row else None
