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

```python
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
```python
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
| in  | element znajduje się w liście/tuple  | 1 in f |
| not in  | element nie znajduje się w liście/tuple  | 1 not in f |

### 1.1 Dodatkowe informacje - id
id obiektu to adres w pamięci komputera przypisany do danej zmiennej.
```python
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

```python
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
```python
if True:
	print("Prawda")
> Prawda

if False:
	print("Prawda")
> 
```
Częstszym użyciem `if` jest sprawdzenie wartości jakiejś zmiennej, na przykład:
```python
jezyk = "Python"

if jezyk == "Python":
	print("poprawny jezyk")
if jezyk != "Python":
	print("niepoprawny jezyk")
```
lub
```python
wiek = 17

if wiek >= 18:
	print("jesteś pełnoletnia")
if wiek < 18:
	print("nie jesteś pełnoletnia")
```
## 3. if-else (_jeśli -- w innym wypadku_)
To wyrażenie działa podobnie do warunku `if`, ale pozwala na łączenie dwóch przeciwstawnych warunków bez konieczności pisania ich dwa razy. Powyższe przykłady możemy zapisać tak:
```python
jezyk = "Python"

if jezyk == "Python":
	print("poprawny jezyk")
else:
	print("niepoprawny jezyk")
```
lub
```python
wiek = 17

if wiek >= 18:
	print("jesteś pełnoletnia")
else:
	print("nie jesteś pełnoletnia")
```

## 4. if-elif-else (_jeśli -- w innym wypadku, jeśli -- w innym wypadku_)
To wyrażenie rozbudowuje warunek `if-else`, umożliwiając dodanie kilku rozłącznych logicznie (wzajemnie wykluczających się) warunków.

Na przykład, jeśli chcemy na podstawie wieku określić, czy użytkowniczka jest małoletnia (<13 lat), niepełnoletnia (13-<18 lat) czy pełnoletnia (>=18) lat, możemy użyć wyrażenia:

```python
wiek = input("podaj swój wiek\n")

if wiek < 13:
	print("jesteś małoletnia")
elif wiek < 18: # już wiemy że wiek nie jest mniejszy od 13, więc `wiek >= 13` na pewno jest prawdziwe
	print("jesteś niepełnoletnia")
else: # już wiemy że `wiek >= 13` i `wiek >=18`
	print("jesteś pełnoletnia")
```
Można używać dowolnie wiele wyrażeń `elif`, i nie ma obowiązku kończenia wyrażenia warunkiem `else`. Ważna jest jedynie, że `else`i `elif` zawsze są rozłączne logicznie wobec wszystich warunków je poprzedzających, oraz że lista warunków musi zacząć się wyrażeniem `if`.

## 5. range (_zakres_)
Funkcja range, opisana [tutaj](https://docs.python.org/3/library/stdtypes.html#range).
```python
a = range(10) # zakres liczb od 0 do 9 (zakres nigdy nie zawiera najwyższej liczby)
b = range(1,10) # zakres liczb od 1 do 9
c = range(1,10,2) # zakres liczb od 1 do 9, co 2 liczbę
```

range() tworzy _obiekt - iterator_ zawierający liczby w danym zakresie i generujący je na żądanie . Aby je wydrukować, należy zmienić dany obiekt na listę.

```python
a = list(range(10))
print(a)
> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = list(range(1,10))
print(b)
> [1, 2, 3, 4, 5, 6, 7, 8, 9]

c = list(range(1,10,2)) 
print(c)
> [1, 3, 5, 7, 9]
```

## 6. for (_dla_)
For to przykład, który umożliwia _iterację_ (powtórzenie zadania) dla każdego elementu jakiegoś zbioru (na przykład listy)

```python
lista = [1, 2, 3, 4]
for el in lista: # el jest umowną zmienną, w którą zapisywany jest konkretny element przy danej iteracji. Może mieć dowolną nazwę.
	print(el)
	
> 1
2
3
4
```

Możemy używać też funkcji `range()`, aby _iterować_ przez kolejne liczby

```python
for i in range(5):
	print("liczba", i)
	
> liczba 0
liczba 1
liczba 2
liczba 3
liczba 4
```

## 7. while (_podczas gdy_)
Pętla `while` wykonuje linie kodu w bloku tuż po zdaniu warunkowym, _dopóki warunek jest spełniony_. Na przykład

```python
i = 0
while i < 4:
	print("numer", i)
	i += 1 # zwiększ i o 1
	
> numer 0
numer 1
numer 2
numer 3
```

Pętla ta jest przydatna na przykład do sprawdzenia haseł podanych przez użytkownika

```python
pin = 1234
haslo = input("Podaj hasło\n")
while pin != haslo:
	print("Błędne hasło.")
	haslo = input("Podaj hasło ponownie.\n") # zaktualizuj zmienną
print("Hasło poprawne") # zostanie wydrukowane dopiero, gdy skońćzy się pętla while 
			# - gdy warunek pin != haslo przestanie byc poprawny (wiec gdy prawda bedzie pin == haslo)
```
Ta pętla będzie powtarzać się w nieskończoność, dopóki hasło nie będzie podane poprawnie.

```
Podaj hasło
> 4321
Błędne hasło.
Podaj hasło ponownie.
> 3982
Błędne hasło.
Podaj hasło ponownie.
.
.
.
Podaj hasło ponownie.
> 1234
Hasło poprawne.

```
