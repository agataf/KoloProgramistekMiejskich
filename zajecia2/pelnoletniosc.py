'''
Zapytaj użytkowniczkę o wiek. Podaj odpowiedź 
"Jesteś małoletnia/Jesteś niepełnoletnia/Jesteś pełnoletnia" 
w zależności od jej wieku (do 13, do 18 lub powyżej 18 lat).

Ile masz lat?
> 17
Jesteś niepełnoletnia.

Ile masz lat?
> 10
Jesteś małoletnia.

Podpowiedź: przyda się tutaj forma if-elif-else
'''

wiek = input("Ile masz lat?\n")

if wiek < 13:
	# jeżeli warunek powyżej jest spełniony, kod w tym miejscu zostanie wykonany
	# a bloki pod pozostałymi pytaniami (elif, else) zostaną zignorowane
	print("Jesteś małoletnia")
elif wiek < 18:
	# jeśli warunek wiek < 13 nie jest spełniony, znaczy to że wiek >= 13
	# więc wystarczy sprawdzić czy wiek < 18 żeby sprawdzić czy leży w zakresie 13-18
	print("Jesteś niepełnoletnia")
else:
	# jeśli żaden z powyższych warunków nie jest spełniony (wiek >= 13 i wiek >= 18):
	print("Jesteś pełnoletnia")