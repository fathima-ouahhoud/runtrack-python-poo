class Operator:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

value = Operator(12, 3)

print(f"Le numero 1 est: {value.numero1}")
print(f"Le numero 2 est: {value.numero2}")