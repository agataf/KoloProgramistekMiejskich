'''
Zapytaj użytkowniczkę jak na na imię, zapisz jej imię do zmiennej a i wydrukuj komunikat:

Jak masz na imię?
> Ania
Ania
Cześć Ania!
'''

# 1. Zapytaj użytkowniczkę o imię
# użyj funkcji input

a = input("Jak masz na imię?")

# 2. Wydrukuj imię

print(a)

# 3. Wydrukuj komunikat Cześć ....!
# podpowiedź

print("Cześć " + a + "!")

# 4. Spróbuj dodać znak "\n" na końcu tekstu w funkcji input. Co zauważasz?
a = input("Jak masz na imię?\n")

# teraz nie musimy wpisywać odpowiedzi w tej samej linijce co pytanie
# \n to znak nowej linijki (jak enter w wordzie)