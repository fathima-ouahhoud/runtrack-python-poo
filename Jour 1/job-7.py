class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

personnage = Personnage(2, 3)
print(personnage.position())

personnage.gauche()
print(personnage.position())

personnage.droite()
print(personnage.position())

personnage.haut()
print(personnage.position())

personnage.bas()
print(personnage.position())
