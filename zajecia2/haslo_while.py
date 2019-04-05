'''
Zapytaj użytkowniczkę o hasło. Jeśli zna poprawne hasło, pozwól jej wejść. Jeśli nie zna, zapytaj o nie ponownie.

Podaj PIN
> 2880
To hasło jest błędne, spróbuj ponownie.

Podaj PIN
> 3729
Pin poprawny! Możesz wejść.
'''

# KOD Z ZADANIA HASLO.PY:

# haslo = 3729
# pin = input("Podaj PIN\n")

# if pin == haslo:
# 	print("Pin poprawny! Możesz wejść!")
# else:
# 	print("To hasło jest błędne.")

# powyższy kod modyfikujemy:

haslo = 3729

# pierwszy raz zapytaj o pin
pin = input("Podaj PIN\n")

# dopóki pin jest nieprawidłowy
while pin != haslo:
	# daj znać użytkowniczce
	print("To hasło jest błędne.")
	# poproś ponownie o pin
	# (jeśli tego nie zrobimy, program w nieskończoność będzie pisał, że hasło jest błędne)
	pin = input("Podaj PIN\n")

# program wyjdzie z pętli while, kiedy pin != hasło przestanie być prawdziwe
# czyli kiedy pin == hasło
# wtedy możemy wpuścić użytkowniczkę
print("Pin poprawny! Możesz wejść!")
	