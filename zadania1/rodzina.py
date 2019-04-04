'''
Ten program zbiera od użytkownika pytania o jego członków rodziny 
i na końcu pisze podsumowanie zebranych informacji.

Cześć! Chciałabym zapytać Cię o Twoją rodzinę.
Jak masz na imię?
> Ania
Jak ma na imię Twoja mama?
> Ewa
A Twój ojciec?
> Adam
Ilu braci/sióstr masz? (Jeśli żadnych, wpisz 0)
>
Jeśli masz rodzeństwo, to jak ma/mają na imiona? (podaj po przecinku, np. Basia, Robert)
>
Ile masz dzieci? (Jeśli żadnych, wpisz 0)
> 1
Jeśli tak, jak ma/mają na imiona? 
> Beata
Masz na imię Ania. Twoja mama ma na imię Ewa, a twój ojciec Adam. Nie masz rodzeństwa. Masz 1 dziecko, nazywa się Beata. 
'''

print("Cześć! Chciałabym zapytać Cię o Twoją rodzinę.")

imie = input("Jak masz na imię?\n")
mama = input("Jak ma na imię Twoja mama?\n")
tata = input("A Twój ojciec?\n")

rodzenstwo_liczba = int(input("Ilu braci/sióstr masz? (Jeśli żadnych, wpisz 0)\n"))

if rodzenstwo_liczba > 0:
	rodzenstwo_imiona = input("Jak ma/mają na imiona?\n")
	

dzieci_liczba = int(input("Ile masz dzieci? (Jeśli żadnych, wpisz 0)\n"))

if dzieci_liczba > 0:
	dzieci_imiona = input("Jak ma/mają na imiona?\n")

odpowiedz = []
odpowiedz.append("Masz na imię " + imie + ".")
odpowiedz.append("Twoja mama ma na imię " + mama + ", a twój ojciec " + tata + ".")

if rodzenstwo_liczba == 0:
	odpowiedz.append("Nie masz rodzeństwa.")
elif rodzenstwo_liczba == 1:
	odpowiedz.append("Masz 1 brata lub siostrę. Nazywa się " + rodzenstwo_imiona + ".")
else:
	odpowiedz.append("Masz " + str(rodzenstwo_liczba) + " rodzenstwa. 	" + \
		 "Nazywają się " + rodzenstwo_imiona + ".")
	

if dzieci_liczba == 0:
	odpowiedz.append("Nie masz dzieci.")
elif dzieci_liczba == 1:
	odpowiedz.append("Masz 1 dziecko. Nazywa się " + dzieci_imiona + ".")
else:
	odpowiedz.append("Masz " + str(dzieci_liczba) + " dzieci. Nazywają się " + dzieci_imiona + ".")

print(' '.join(odpowiedz))
