from kalkulator import Kalkulator
import math


class ZaawansowanyKalkulator(Kalkulator):
    def __init__(self):
        super().__init__()

    def pierwiastek(self, a):
        if a < 0:
            return "Pierwiastek z liczby ujemnej jest niezdefiniowany!"
        return math.sqrt(a)
