import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Cercle de rayon : {self.rayon}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)

for cercle in [cercle1, cercle2]:
    cercle.afficherInfos()
    print(f"Circonférence : {cercle.circonference():.2f}")
    print(f"Diamètre : {cercle.diametre()}")
    print(f"Aire : {cercle.aire():.2f}")
    print()