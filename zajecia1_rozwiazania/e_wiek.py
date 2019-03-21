'''
Zapytaj użytkowniczkę jak na na imię, i ile ma lat i wydrukuj komunikat:

Jak masz na imię?
> Ania
Cześć Ania!
Ile masz lat?
> 32
Ania, urodziłaś się w 1987 roku.
'''

# Zapytaj użytkowniczkę o imię
imie = input("Jak masz na imię?")

# Wydrukuj komunikat
print("Cześć " + a + "!")

# Zapytaj użytkowniczkę o wiek
wiek = input("Ile masz lat?")

# sprawdź jakiego typu jest otrzymana zmienna - użyj funkcji type()
print(type(wiek))

# typ jest stringiem, mimo że oczekiwałyśmy liczby! 
# czemu? bo to, co wpisuje użytkownik z założenia jest tekstem
# musimy zmienić typ, żeby móc używać tej liczby do obliczeń.


# Jeśli trzeba, zmień typ, tak żebyśmy mogły wykonywać na niej działania

wiek = int(wiek)

# oblicz jej rok urodzenia
rok = 2019 - wiek

# zamień go z powrotem na string, żebyśmy mogły go wydrukować

rok = str(rok)

# wydrukuj komunikat końcowy
print(imie +", urodziłaś się w " + str(rok) + " roku.")

# linie 31-41 można zastąpić:
# print(imie +", urodziłaś się w " + str(2019 - int(wiek)) + " roku.")


