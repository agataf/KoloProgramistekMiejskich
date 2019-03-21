'''
Łączenie stringów.
'''
a = "Dzień"
b = "dobry"
c = "Jestem"
# zmień na swoje imię
d = "Agata"

# 1. wydrukuj komunikat "Dzień dobry", używając zmiennych a i b

print(a + " " + b)

# lub print(a,b)

# 2. wydrukuj komunikat "Jestem ...", używając zmiennych c i d

print(c + " " + d)

# lub print(c,d)

# 3. Wydrukuj komunikat "Mam 23 lata" używając zmiennych poniżej
a = "Mam"
b = "23"
c = "lata"

print(a,b,c)

# 4. Użyj innych zmiennych
a = "Mam"
b = 29 # czym różni się ten przypadek od podwyższego?
c = "lat"

# print(a + " " + b + " " + c) zwraca błąd (TypeError!)

# 5. użyj funkcji type() żeby sprawdzić typ zmiennych a, b, c

print(type(b))

# co zauważasz?

# 6. Wydrukuj komunikat "Mam 25 lat" używając a, b, c

# musimy zmienić typ b!
b_string = str(b)

print(a + " " + b_string + " " + c)

# można to też zrobić od razu:

print(a + " " + str(b) + " " + c)


