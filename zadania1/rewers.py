'''
Przyjmij od użytkowniczki 5 słów, zwróć je w odwróconej kolejności.

Podaj 5 słów
> Kodowanie jest wlasciwie calkiem latwe
latwe calkiem wlasciwie jest kodowanie
'''

slowa = input("podaj pięć słów\n")

slowa = slowa.split(' ')

print("metoda 1:", slowa[4], slowa[3], slowa[2], slowa[1], slowa[0])

# można też użyć funkcji reverse

slowa.reverse()

print("metoda 2:", slowa[0], slowa[1], slowa[2], slowa[3], slowa[4])