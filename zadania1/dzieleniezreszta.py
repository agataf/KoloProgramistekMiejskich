'''
Zapytaj użytkownika o dwie liczby, które chcesz podzielić. Podaj w odpowiedzi wynik dzielenia z resztą.

Podaj liczbę, którą chcesz podzielić
> 27
Przez jaką liczbę chcesz podzielić 27?
> 6
27/6 = 4 reszta 3
'''

liczba = input("Podaj liczbę, którą chcesz podzielić\n")

liczba = int(liczba)

dzielnik = input("Przez jaką liczbę chcesz podzielić " + str(liczba) + "?\n")

dzielnik = int(dzielnik)

calosci = liczba // dzielnik # albo int(liczba/dzielnik)

reszta = liczba % dzielnik

print(str(liczba) + "/" + str(dzielnik) + " = " + str(calosci) + " reszta " + str(reszta))
