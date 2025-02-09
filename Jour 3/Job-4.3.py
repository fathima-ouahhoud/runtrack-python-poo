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

class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Joueur {self.nom} (#{self.numero}, {self.position}) - Buts: {self.buts}, Passes: {self.passes}, Cartons jaunes: {self.cartons_jaunes}, Cartons rouges: {self.cartons_rouges}")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom, action):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton rouge":
                    joueur.recevoirUnCartonRouge()
                break

barca = Equipe("FC Barcelone")
real = Equipe("Real Madrid")
messi = Joueur("Messi", 10, "Attaquant")
benzema = Joueur("Benzema", 9, "Attaquant")
barca.ajouterJoueur(messi)
real.ajouterJoueur(benzema)
messi.marquerUnBut()
benzema.recevoirUnCartonJaune()
tprint("Statistiques des joueurs de Barcelone:")
barca.afficherStatistiquesJoueurs()
print("Statistiques des joueurs du Real Madrid:")
real.afficherStatistiquesJoueurs()
