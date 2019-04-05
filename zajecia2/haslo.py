'''
Zdefiniuj swoje hasło (np. `haslo = 3729`). Zapytaj użytkowniczkę o hasło. Jeśli zna poprawne hasło, pozwól jej wejść. Jeśli nie zna, powiedz że hasło jest błędne.

Podaj PIN
> 2880
To hasło jest błędne.

Podaj PIN
> 3729
Pin poprawny! Możesz wejść.
'''

haslo = 3729
pin = input("Podaj PIN\n")

if pin == haslo:
	print("Pin poprawny! Możesz wejść!")
else:
	print("To hasło jest błędne.")