''' połącz imię pierwszej osoby z nazwiskiem drugiej używając ich zmiennych

przykład
a = "Anna Nowak"
b = "Monika Kowalska"

Anna Kowalska
Monika Nowak

Używając indeksów
'''

a = "Anna Nowak"
b = "Monika Kowalska"

# spróbuj wydrukować pierwszy, drugi, piąty znak a

print(a[0], a[1], a[4])
# pamiętaj że w informatyce liczymy od 0!

# spróbuj wydrukować ostatni znak a
print(a[-1])

# spróbuj wydrukować pierwsze 5 znaków a
print(a[:5])
# lub print a[0:5]

# spróbuj wydrukować ostatnie 5 znaków b
print(b[-5:])
# lub print(a[-5:-1])


# spróbuj podzielić a na a_imie i a_nazw używając indeksów
a_imie = a[:4]
a_nazw = a[-5:]
b_imie = b[:6]
b_nazw = b[-8:]

# połącz a_imie i b_nazw i wydrukuj
ab = a_imie + " " + b_nazw
print(ab)

# połącz b_imie i a_nazw i wydrukuj
ba = b_imie + " " + a_nazw
print(ba)

