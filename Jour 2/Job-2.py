class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre  
        self.__auteur = auteur  
        self.__nombre_pages = nombre_pages if isinstance(nombre_pages, int) and nombre_pages > 0 else 0  

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_pages(self, nombre_pages):
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self.__nombre_pages = nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def afficher(self):
        print(f"Livre -> Titre: {self.__titre}, Auteur: {self.__auteur}, Pages: {self.__nombre_pages}")

livre1 = Livre("Le petit prince", "Antoine de Saint-Exupéry", 96)
livre1.afficher()
livre1.set_titre("Le petit prince")
livre1.set_auteur("Antoine de Saint-Exupéry")
livre1.set_nombre_pages(48)
livre1.afficher()
livre1.set_nombre_pages(-50) 
livre1.afficher()
