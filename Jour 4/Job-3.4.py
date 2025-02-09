class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  
        self.__largeur = largeur 

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur) 
        self.__hauteur = hauteur  

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur 

rect = Rectangle(10, 5)
print("Longueur du rectangle:", rect.get_longueur())
print("Largeur du rectangle:", rect.get_largeur())
print("Périmètre du rectangle:", rect.perimetre())
print("Surface du rectangle:", rect.surface())

rect.set_longueur(15)
rect.set_largeur(7)
print("\nAprès modification des dimensions :")
print("Nouvelle longueur:", rect.get_longueur())
print("Nouvelle largeur:", rect.get_largeur())
print("Nouveau périmètre:", rect.perimetre())
print("Nouvelle surface:", rect.surface())

para = Parallelepipede(10, 5, 8)
print("\nParallélépipède :")
print("Longueur:", para.get_longueur())
print("Largeur:", para.get_largeur())
print("Hauteur:", para.get_hauteur())
print("Surface du parallélépipède:", para.surface())
print("Volume du parallélépipède:", para.volume())

para.set_hauteur(10)
print("\nAprès modification de la hauteur :")
print("Nouvelle hauteur:", para.get_hauteur())
print("Nouveau volume:", para.volume())
