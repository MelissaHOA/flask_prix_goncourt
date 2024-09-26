class Selection:
    def __init__(self, date_selection, id_livre, vote):
        self.date_selection = date_selection
        self.id_livre = id_livre
        self.vote = vote

    def __str__(self):
        return f"Sélection: Date {self.date_selection}, ID Livre: {self.id_livre}, Vote: {self.vote}"


