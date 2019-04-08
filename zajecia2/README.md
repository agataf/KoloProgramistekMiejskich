# Zajęcia 2
Na tych zajęciach nauczymy się wyrażeń logicznych i pętli w Pythonie.

Dużo przydatnych informacji znajdziecie też tutaj:
https://pl.python.org/docs/tut/node6.html

## 1. booleans (wartości zerojedynkowe)
Na poprzednich zajęciach wspomniałyśmy o `bool` (boolean, wartość zerojedynkowa) jako jednego z typu danych 

| rodzaj | Znaczenie | Przykład|
| ------------- | ------------- | ------------- |
| int  | integer - liczba naturalna | `5` |
| float  | liczba rzeczywista (z miejscami po przecinku)  | `5.`, `6.001`,  |
| str  | string - słowo  | `"hello"`, `"5"` |
| bool | wartość zerojedynkowa | `True`, `False` | 


`bool` ma tylko dwie możliwe wartości: `True` (prawda) lub `False` (fałsz).

`bool` są przydatne, gdy próbujemy porównać wartości za pomocą równań i nierówności, np:

```
a = True
print(type(a))
> bool
print(a)
> True

b = (5 == 6)
print(type(b))
> bool
print(b)
> False

c = 675
d = (683 <= c)
print(d)
> False
```

Do porównań używamy następujących znaków:
```
a = 10
b = 11
c = [2]
d = [2]
e = d
f = [1,3,5]
```
| Znak | Znaczenie | Przykład (z wynikiem True) |
| ------------- | ------------- | ------------- |
| ==  | jest równe  | a == (b-1) |
| !=  | nie jest równe  | a != b |
| >  | większe niż  | a > 9 |
| >=  | większe lub równe | a >= 10 | 
| <  | mniejsze niż  | a < 11 |
| <=  | mniejsze lub równe  | a <= 11 |
| and | oraz - łączenie dwóch wyrażeń | (a == 10) and (b == 11) |
| or  | lub - łączenie dwóch wyrażeń  | (a == 10) or (a == 11) |
| is in  | element znajduje się w liście/tuple  | 1 is in f |

### 2.1 Dodatkowe informacje - id
id obiektu to adres w pamięci komputera przypisany do danej zmiennej.
```
a = [2]
b = [2]
print(a==b)
> True
print(a is b)
> False
print(id(a)) # różne za każdym użyciem programu - zmienne są zapisywane na bieżąco w najbardziej optymalnym miejscu w pamięci
> 4358003784
print(id(b))
> 4359207176
```

| Znak | Znaczenie | Przykład (z wynikiem True) |
| ------------- | ------------- | ------------- |
| is  | dwa obiekty mają to samo id | e is d |
| is not  | dwa obiekty mają inne id  | c is not d |

Może się zdarzyć wyjątek, że dwie zmienne o równych wartościach mają to samo id - bo komputer, by oszczędzić miejsce, zapisał wartość zmiennej w jednym miejscu w pamięci, i nazwy obu zmiennych wskazują na to miejsce. Jeśli chcecie poczytać więcej na ten temat, poczytajcie wikipedię: https://pl.wikipedia.org/wiki/Wska%C5%BAnik_(typ_danych)

```
a = 2
b = 2
print(a is b)
> True 
# bo 2 to często używana liczba - jest już w pamięci

a = 10393
b = 10393
print(a is b)
> False
# bo 10393 to rzadko używana liczba - nie ma jej w pamięci
```

## 2. if (_jeśli_)
wyrażenie `if` sprawdza czy warunek jest prawdziwy i:
- jeśli warunek jest prawdziwy (ma wartość `True`), wykonywane są czynności bezpośrednio po warunku, w bloku kodu gdzie każda linia zaczyna się tabem)
- jeśli nie jest prawdziwy, omija ten blok i zaczyna wykonywać linie kodu znajdujące się po tym bloku.

Możemy po prostu użyć wartości `True` i `False` w warunku - ten kod będzie jednak zawsze działał tak samo (jego działanie nie będzie zależne od zmiany wartości innych zmiennych).
```
if True:
	print("Prawda")
> Prawda

if False:
	print("Prawda")
> 
```
Częstszym użyciem `if` jest sprawdzenie wartości jakiejś zmiennej, na przykład:
```
jezyk = “Python”

if jezyk == “Python”:
	print(“poprawny jezyk”)
if jezyk != “Python”:
	print(“niepoprawny jezyk”)
```
lub
```
wiek = 17

if wiek >= 18:
	print(“jesteś pełnoletnia”)
if wiek < 18:
	print(“nie jesteś pełnoletnia”)
```
## if-else (_jeśli -- w innym wypadku_)
To wyrażenie działa podobnie do warunku `if`, ale pozwala na łączenie dwóch przeciwstawnych warunków bez konieczności pisania ich dwa razy. Powyższe przykłady możemy zapisać tak:
```
jezyk = “Python”

if jezyk == “Python”:
	print(“poprawny jezyk”)
else:
	print(“niepoprawny jezyk”)
```
lub
```
wiek = 17

if wiek >= 18:
	print(“jesteś pełnoletnia”)
else:
	print(“nie jesteś pełnoletnia”)
```

## if-elif-else (_jeśli -- w innym wypadku, jeśli -- w innym wypadku_)
To wyrażenie rozbudowuje warunek `if-else`, umożliwiając dodanie kilku rozłącznych logicznie (wzajemnie wykluczających się) warunków.

Na przykład, jeśli chcemy na podstawie wieku określić, czy użytkowniczka jest małoletnia (<13 lat), niepełnoletnia (13-<18 lat) czy pełnoletnia (>=18) lat, możemy użyć wyrażenia:

```
wiek = input("podaj swój wiek\n")

if wiek < 13:
	print(“jesteś małoletnia”)
elif wiek < 18: # już wiemy że wiek nie jest mniejszy od 13, więc `wiek >= 13` na pewno jest prawdziwe
	print(“jesteś niepełnoletnia”)
else: # już wiemy że `wiek >= 13` i `wiek >=18`
	print(“jesteś pełnoletnia”)
```
Można używać dowolnie wiele wyrażeń `elif`, i nie ma obowiązku kończenia wyrażenia warunkiem `else`. Ważna jest jedynie, że `else`i `elif` zawsze są rozłączne logicznie wobec wszystich warunków je poprzedzających, oraz że lista warunków musi zacząć się wyrażeniem `if`.

## range (_zakres_)
Funkcja range, opisana [tutaj](https://docs.python.org/3/library/stdtypes.html#range)
## for (_dla_)
For to przykład, który umożliwia _iterację_ (powtórzenie zadania) dla każdego elementu jakiegoś zbioru (na przykład listy)

```
lista = [1, 2, 3, 4]
for el in lista:
	print(el)
```

## while (_podczas gdy_)
