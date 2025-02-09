class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque 
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationVehicule(self):
        print(f"Maque = {self.marque}")
        print(f"Modele = {self.modele}")
        print(f"Annee = {self.annee}")
        print(f"Prix = {self.prix}")

    def demarrer(self):
        print("Attention, je roule")

Vehicule
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationVehicule(self):
        super().informationVehicule()
        print(f"Nombre de porte = {self.portes}")

    def demarrer(self):
        print("La voiture démarre")


Vehicule
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2

    def informationVehicule(self):
        super().informationVehicule()
        print(f"Nombre de roues = {self.roues}")

    def demarrer(self):
        print("La moto demarre")

if __name__ == "__main__":
    voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
    print("Information de la voiture:")
    voiture.informationVehicule()
    voiture.demarrer()

    moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
    print("\nInformation de la moto:")
    moto.informationVehicule()
    moto.demarrer