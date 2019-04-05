'''
Zauważ że po samym roku nie można podać dokładnego wieku. Jeśli ktoś ma urodziny np. w sierpniu, błędnie założymy, że ma już tyle lat, ile wynikałoby z roku urodzenia.

Zapytaj użytkowniczkę jak na na imię, i ile ma lat i wydrukuj komunikat:

Jak masz na imię?
> Ania
Ile masz lat?
> 32
Czy miałaś już urodziny w tym roku? (tak/nie)
> nie
Ania, urodziłaś się w 1986 roku.
'''

imie = input("Jak masz na imię?\n")

wiek = input("Ile masz lat?\n")

urodziny = input("Czy miałaś już urodziny w tym roku? (tak/nie)")

if urodziny == "tak":
	rok = 2019 - int(wiek)
else:
	rok = 2018 - int(wiek)

print(imie + ", urodziłaś się w " + str(rok) + " roku.")