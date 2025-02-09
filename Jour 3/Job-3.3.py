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

class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquer_comme_finie(self):
        self.statut = "terminée"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [tache for tache in self.taches if tache.titre != titre]

    def afficherListe(self):
        return [(t.titre, t.description, t.statut) for t in self.taches]

    def filterListe(self, statut):
        return [(t.titre, t.description) for t in self.taches if t.statut == statut]

tache1 = Tache("Acheter du pain", "Aller à la boulangerie")
tache2 = Tache("Faire du sport", "Aller courir 30 minutes")
tache3 = Tache("Lire un livre", "Lire 20 pages du roman")
liste_taches = ListeDeTaches()
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)
tache1.marquer_comme_finie()
liste_taches.supprimerTache("Faire du sport")
print("Toutes les tâches:", liste_taches.afficherListe())
print("Tâches à faire:", liste_taches.filterListe("à faire"))
