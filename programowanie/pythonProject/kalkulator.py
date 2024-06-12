class Kalkulator:
    def __init__(self):
        pass

    def dodaj(self, a, b):
        return a + b

    def odejmij(self, a, b):
        return a - b

    def mnoz(self, a, b):
        return a * b

    def dziel(self, a, b):
        if b == 0:
            return "Nie można dzielić przez zero!"
        return a / b



