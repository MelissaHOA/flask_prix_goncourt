class Livre:
    def __init__(self, id_livre, titre, auteur, resume_livre, prix):
        self.id_livre = id_livre
        self.titre = titre
        self.auteur = auteur
        self.resume_livre = resume_livre
        self.prix = prix

    def __str__(self):
        return f"Livre: {self.titre} de {self.auteur}"


