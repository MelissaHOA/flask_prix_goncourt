import sqlite3
from models.membre import Membre
from typing import List

class MembresDAO:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def get_all_membres(self) -> List[Membre]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM le_prix_goncourt_membres"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Membre(*row) for row in rows]

    def get_membre_by_id(self, id_membre: int) -> Membre:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM le_prix_goncourt_membres WHERE id_membre = ?"
            cursor.execute(query, (id_membre,))
            row = cursor.fetchone()
            return Membre(*row) if row else None
