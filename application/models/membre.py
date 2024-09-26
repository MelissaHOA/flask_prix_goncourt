class Membre:
    def __init__(self, id_membre, nom_prenom_membre, id_fonction):
        self.id_membre = id_membre
        self.nom_prenom_membre = nom_prenom_membre
        self.id_fonction = id_fonction

    def __str__(self):
        return f"Membre: {self.nom_prenom_membre} "
