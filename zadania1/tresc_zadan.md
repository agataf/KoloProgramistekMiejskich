Treść zadań:

## POZIOM 1:
### 1. POLE
Napisz program który prosi użytkownika o promien okregu i oblicza jego pole.
Przyklad:
```
jaki promien ma twoj okrag?
> 5
Twój okrąg ma pole 75.39
```

## POZIOM 2:
### 1. DZIELENIE Z RESZTA
Zapytaj użytkownika o dwie liczby, które chcesz podzielić. 
Podaj w odpowiedzi wynik dzielenia z resztą.
```
Podaj liczbę, którą chcesz podzielić
> 27
Przez jaką liczbę chcesz podzielić 27?
> 6
27/6 = 4 reszta 3
```
Podpowiedź: sprawdź w dokumentacji pythona różnicę między / i //, oraz znak %

### 2. KALKULATOR
Stwórz program-kalkulator, który będzie traktował znak & jako znak mnożenia.
```
Podaj działanie
>2&8
16
>2&-8
-16
```
podpowiedź: `split()` definiując na jakim znaku powinien być dzielony string
https://docs.python.org/3/library/stdtypes.html#str.split


### 3. REWERS
Przyjmij od użytkowniczki 5 słów, zwróć je w odwróconej kolejności.
```
Podaj 5 słów
> Kodowanie jest wlasciwie calkiem latwe
latwe calkiem wlasciwie jest kodowanie

Wersja trudniejsza: spróbuj użyć tylko jednej zmiennej: listy.
Przyda ci się funkcja append
```
https://www.tutorialspoint.com/python/list_append.htm

## POZIOM 3:
## 1. RODZINA
Ten program zbiera od użytkownika pytania o jego członków rodziny
i na końcu pisze podsumowanie zebranych informacji.

```
Cześć! Chciałabym zapytać Cię o Twoją rodzinę.
Jak masz na imię?
> Ania
Jak ma na imię Twoja mama?
> Ewa
A Twój ojciec?
> Adam
Ilu braci/sióstr masz? (Jeśli żadnych, wpisz 0)
>
Jeśli masz rodzeństwo, to jak ma/mają na imiona?
>
Ile masz dzieci? (Jeśli żadnych, wpisz 0)
> 1
Jeśli tak, jak ma/mają na imiona?
> Beata
Masz na imię Ania. Twoja mama ma na imię Ewa, a twój ojciec Adam. Nie masz rodzeństwa. Masz 1 dziecko, nazywa się Beata. 
```
Uwaga: tutaj konieczne będzie użycie "conditional statement", jak na przykład:
```
if a = 5:
	print("a to 5")
	b = a+b
```
aby zrozumieć je lepiej, poszukajcie podpowiedzi online.
https://www.tutorialspoint.com/python/python_if_else.htm
