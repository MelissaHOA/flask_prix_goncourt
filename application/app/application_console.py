class ApplicationConsole:
    def __init__(self, selection_service):
        self.selection_service = selection_service

    def menu(self):
        while True:
            print("1. Afficher les livres de la première sélection")
            print("2. Afficher les livres de la deuxième sélection")
            print("3. Afficher les livres de la troisième sélection")
            print("0. Quitter")
            choix = input("Votre choix : ")

            if choix == "1":
                livres = self.selection_service.get_livres_premiere_selection()
                self.afficher_livres(livres)
            elif choix == "2":
                livres = self.selection_service.get_livres_deuxieme_selection()
                self.afficher_livres(livres)
            elif choix == "3":
                livres = self.selection_service.get_livres_troisieme_selection()
                self.afficher_livres(livres)
            elif choix == "0":
                break

    def afficher_livres(self, livres):
        for livre in livres:
            print(livre)
