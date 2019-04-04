'''
Stwórz program-kalkulator, który będzie traktował znak & jako znak mnożenia.

Podaj działanie
>2&8
16
>2&-8
-16
'''

dzialanie = input("Podaj działanie\n")

liczby = dzialanie.split('&')

wynik = float(liczby[0]) * float(liczby[1])

print(wynik)