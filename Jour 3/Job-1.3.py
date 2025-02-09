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

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print(f"Population de la ville de {paris.get_nom()}: {paris.get_population()} habitants")
print(f"Population de la ville de {marseille.get_nom()}: {marseille.get_population()} habitants")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print(f"Mise à jour de la population de la ville de {paris.get_nom()}: {paris.get_population()} habitants")
print(f"Mise à jour de la population de la ville de {marseille.get_nom()}: {marseille.get_population()} habitants")
