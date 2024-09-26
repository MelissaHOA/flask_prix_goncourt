import sqlite3
from models.selection import Selection
from typing import List

class SelectionDAO:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def get_selection_by_date(self, selection_date: str) -> List[Selection]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM le_prix_goncourt_selectionner WHERE date_selection = ?"
            cursor.execute(query, (selection_date,))
            rows = cursor.fetchall()
            return [Selection(*row) for row in rows]

    def get_votes_by_livre(self, id_livre: int) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "SELECT vote FROM le_prix_goncourt_selectionner WHERE id_livre = ?"
            cursor.execute(query, (id_livre,))
            vote = cursor.fetchone()
            return vote[0] if vote else 0
