import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    def aire(self):
        return self.largeur * self.hauteur

Forme
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    def aire(self):
        return math.pi * self.radius**2

if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print("Aire du rectangle:", rect.aire())

    cercle = Cercle(7)
    print("Aire du cercle:", cercle.aire())
