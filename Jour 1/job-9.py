class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Produit : {self.nom}, Prix HT : {self.prixHT}, TVA : {self.TVA}%, Prix TTC : {self.CalculerPrixTTC():.2f}"

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

produit1 = Produit("Ordinateur", 800, 20)
produit2 = Produit("Smartphone", 500, 20)

print(produit1.afficher())
print(produit2.afficher())

produit1.modifierNom("PC Portable")
produit1.modifierPrix(850)

produit2.modifierNom("Téléphone Haut de Gamme")
produit2.modifierPrix(550)

print(produit1.afficher())
print(produit2.afficher())
