'''
Zapytaj użytkowniczkę jak na na imię, i ile ma lat i wydrukuj komunikat:

Jak masz na imię?
> Ania
Ile masz lat?
> 32
Czy miałaś już urodziny w tym roku? (tak/nie)
> jhhf
To jest błędna odpowiedź. Podaj odpowiedź tak lub nie.
Czy miałaś już urodziny w tym roku? (tak/nie)
> nie
Ania, urodziłaś się w 1986 roku.
'''

# Zapytaj użytkowniczkę o imię
imie = input()

# Zapytaj użytkowniczkę o wiek
wiek = int(input())

# Zapytaj użytkowniczkę o urodziny
urodz = input()

# wydrukuj komunikat końcowy
print()

# dopóki zmienna urodz jest czymś innym niż tekst "tak" lub "nie"
while urodz not in ["",""]:
  # Napisz, że odpowiedź powinna brzmieć "tak" lub "nie"
  print()
  # poproś jeszcze raz o odpowiedź
  urodz = 


# oblicz jej rok urodzenia, biorąc pod uwagę czy miała już urodziny
if ....:
  rok = 
elif ....:
  rok =
else:
  print()