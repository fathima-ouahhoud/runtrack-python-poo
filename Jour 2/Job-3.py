class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre 
        self.__auteur = auteur  
        self.__nombre_pages = nombre_pages if isinstance(nombre_pages, int) and nombre_pages > 0 else 0 
        self.__disponible = True 

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

    def verification(self):
        return self.__disponible
    def emprunter(self):
        if self.verification(): 
            self.__disponible = False
            print(f"Le livre '{self.__titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.__titre}' n'est pas disponible.")

    def rendre(self):
        if not self.verification(): 
            self.__disponible = True
            print(f"Le livre '{self.__titre}' a été rendu.")
        else:
            print(f"Le livre '{self.__titre}' n'a pas été emprunté, il est déjà disponible.")

    def afficher(self):
        dispo = "Oui" if self.__disponible else "Non"
        print(f"Livre -> Titre: {self.__titre}, Auteur: {self.__auteur}, Pages: {self.__nombre_pages}, Disponible: {dispo}")

livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
livre1.afficher()
print("Disponible ?", livre1.verification())  
livre1.emprunter()
print("Disponible ?", livre1.verification())  
livre1.emprunter()
livre1.rendre()
print("Disponible ?", livre1.verification()) 
True

livre1.rendre()
