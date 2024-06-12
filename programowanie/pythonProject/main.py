from kalkulator import Kalkulator



kalkulator = Kalkulator()
print(kalkulator.dodaj(5, 3))  #  8
print(kalkulator.odejmij(10, 4))  #  6
print(kalkulator.mnoz(6, 7))  #  42
print(kalkulator.dziel(15, 3))  # 5.0
print(kalkulator.dziel(10, 0))  # Nie można dzielić przez zero!




from zaawansowany import ZaawansowanyKalkulator

zaawansowany_kalkulator = ZaawansowanyKalkulator()
print(zaawansowany_kalkulator.dodaj(5, 3))
print(zaawansowany_kalkulator.pierwiastek(16))
print(zaawansowany_kalkulator.pierwiastek(-4))



kalkulator1 = Kalkulator()
kalkulator2 = Kalkulator()

print(kalkulator1.dodaj(1, 2))  # 3
print(kalkulator2.mnoz(3, 4))  # 12

