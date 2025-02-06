class Operator:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def Addition(self):
        return(self.numero1 + self.numero2)   

value = Operator(12, 3)
resultat = value.Addition()

print(f"{resultat}")