class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque 
        self.__modele = modele  
        self.__annee = annee
        self.__kilometrage = kilometrage  
        self.__en_marche = False 
        self.__reservoir = 50  
        
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def set_reservoir(self, niveau):
        if isinstance(niveau, (int, float)) and 0 <= niveau <= 50:
            self.__reservoir = niveau
        else:
            print("Erreur : Le niveau du réservoir doit être compris entre 0 et 50 litres.")

    def __verifier_plein(self):
        return self.__reservoir
    def demarrer(self):
        if self.__verifier_plein() > 5: 
            print("La voiture démarre.")
        else:
            print("Impossible de démarrer, réservoir insuffisant !")

    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")
    def afficher(self):
        etat = "En marche" if self.__en_marche else "À l'arrêt"
        print(f"Voiture -> Marque: {self.__marque}, Modèle: {self.__modele}, Année: {self.__annee}, Kilométrage: {self.__kilometrage} km, Réservoir: {self.__reservoir} L, État: {etat}")

voiture1 = Voiture("Toyota", "Corolla", 2020, 50000)
voiture1.afficher()
voiture1.demarrer()
voiture1.afficher()
voiture1.set_reservoir(3)
voiture1.demarrer()
voiture1.arreter()
voiture1.afficher()