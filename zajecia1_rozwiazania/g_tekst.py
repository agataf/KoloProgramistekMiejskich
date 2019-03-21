''' połącz imię pierwszej osoby z nazwiskiem drugiej używając ich zmiennych

przykład
a = "Anna Nowak"
b = "Monika Kowalska"

Anna Kowalska
Monika Nowak
'''

a = "Anna Nowak"
b = "Monika Kowalska"

# spróbuj podzielić a na dwa człony (użyj a.split())

# wydrukuj nowo powstałą zmienną
print(a.split())

# sprawdź jej typ
print(type(a.split()))
# o listach będziemy uczyć się więcej na następnych zajęciach
# indeksuje się je tak samo jak stringi!


# używając split i indeksów, spróbuj podzielić a na a_imie i a_nazw
a_imie = a.split()[0]
a_nazw = a.split()[1]
b_imie = b.split()[0]
b_nazw = b.split()[1]

# sprawdź czy otrzymane zmienne wyglądają tak, jak tego chcesz
print(a_imie)
print(a_nazw) 
print(b_imie)
print(b_nazw)


# połącz a_imie i b_nazw i wydrukuj
ab = a_imie + " " + b_nazw
print(ab)

# połącz b_imie i a_nazw i wydrukuj
ba = b_imie + " " + a_nazw
print(ba)