class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population
    
    def ajouter_habitant(self):
        self.__population += 1
    
    def get_population(self):
        return self.__population
    
    def get_nom(self):
        return self.__nom

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouter_habitant()

class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte {self.__numero} - Titulaire: {self.__nom} {self.__prenom} - Solde: {self.__solde} €")

    def afficherSolde(self):
        print(f"Solde du compte {self.__numero}: {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde: {self.__solde} €")

    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Solde insuffisant pour effectuer le retrait.")
        else:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde: {self.__solde} €")

    def agios(self):
        if self.__solde < 0:
            self.__solde -= 10
            print(f"Agios appliqués. Nouveau solde: {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Virement refusé. Solde insuffisant.")
        else:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.__numero}.")

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)
print(f"Population de la ville de {paris.get_nom()}: {paris.get_population()} habitants")
print(f"Population de la ville de {marseille.get_nom()}: {marseille.get_population()} habitants")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)
print(f"Mise à jour de la population de la ville de {paris.get_nom()}: {paris.get_population()} habitants")
print(f"Mise à jour de la population de la ville de {marseille.get_nom()}: {marseille.get_population()} habitants")

compte1 = CompteBancaire(12345, "Dupont", "Jean", 500)
compte2 = CompteBancaire(67890, "Martin", "Sophie", -100, True)

compte1.afficher()
compte2.afficher()
compte1.virement(compte2, 100)
compte1.afficherSolde()
compte2.afficherSolde()
