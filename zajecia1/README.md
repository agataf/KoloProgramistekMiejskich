# Zajęcia 2

## 1. Repl.it
Przez pierwsze kilka zajęć będziemy używać strony repl.it do naszych programów. Strona ta umożliwia używanie pythona w przeglądarce, bez potrzeby ściągania żadnych programów.

Zanim zaczniemy, załóżcie konta na repl.it, żeby móc zapisać swój kod.

Aby otworzyć nowy plik, kliknijcie przycisk "new repl" w prawym górnym rogu, i wybierzcie Python z listy języków.

## 2. Twój pierwszy program
```python
print(“Hello World!”)
> Hello World!
```
Żeby włączyć program, naciśnijcie przycisk start. Aby go zatrzymać, naciśnijcie stop.
![Start-stop](http://pythonic.zoomquiet.top/data/20161110214330/jetfwr4.gif)

cudzysłowia są bardzo ważne! Jeśli spróbujemy zrobić to samo bez cudzysłowia, program zwróci nam błąd `invalid syntax` (niepoprawna składnia)

```
print(Hello World!)

>  File "<ipython-input-46-734633aabfd1>", line 1
    print(Hello World!)
                    ^
SyntaxError: invalid syntax
```
## 3. Komentarze
```python
# Jeżeli na początku linijki podamy kratkę
# Możemy napisać tam cokolwiek
# Jest to bardzo przydatne do opisywania swoich programów
#
# wydrukuj Hello World!
# print(“Hello World!”)

> 
```


## 4. Zmienne

| rodzaj | Znaczenie | Przykład|
| ------------- | ------------- | ------------- |
| int  | integer - liczba naturalna | `5` |
| float  | liczba rzeczywista (z miejscami po przecinku)  | `5.`, `6.001`,  |
| str  | string - słowo  | `"hello"`, `"5"` |
| bool | wartość zerojedynkowa | `True`, `False` | 
| list | lista | `[1,2,3,4]` | 
| range | zakres | `range(0,3)` | 

### 4.0 Zapisywanie zmiennych w Pythonie
Każdy typ zmiennej możemy zapisać w Pythonie tak jak zmienne w matematyce - przypisując wartość po prawej stronie nawiasu, i nazwę zmiennej po lewej:
```python
mojaZmienna = 5
zmienna_1 = "Mój string"
c = 8.5

print(mojaZmienna)
> 5
print(zmienna_1)
> Mój string
print(c)
> 8.5
```
Nazwy zmiennych mogą być dowolne, jednak **nie mogą zaczynać się cyfrą** (np. `1zmienna`).

### 4.1 Int
Int (Integer, liczba całkowita, czyli inaczej każda liczba bez ułamka) to jeden z najprostszych typów danych w pythonie. Inty możemy wykorzystywać do robienia obliczeń, jak w kalkulatorze (pełna lista operacji znajduje się [tutaj](#operacje-na-intach-i-floatach)):
```python
a = 5 + 6
print(a)
> 11

b = 5
c = b * 6
print(c)
> 30
```
### 4.2 Float
Float (z angielskiego _floating point number_) to zmienne, które zawierają część "po przecinku" (może ona wynosić 0).
```python
a = 5.0
b = 1.1

print(a+b)
> 6.1
```
W naszej wersji Pythona (3.x) wynikiem dzielenia dwóch intów będzie zawsze float:
```python
a = 7
b = 2
print(a/b)
> 3.5
```
Wynikiem operacji na incie i floacie zawsze będzie float:
```python
a = 5.0
b = 6
print(a*b)
> 30.0
```

### 4.3 String 
String (inaczej Napis) to typ zmiennej który jest traktowany jako słowo/zdanie. Aby stworzyć zmienną typu string, należy zapisać ją w cudzysłowiach (pojedynczych lub podwójnych).
```python
a = "Hello" # zapisujemy 
b = 'Hello'
print(a)
> Hello
print(b)
> Hello
```
#### 4.3.1 Typy cudzysłowów
Aby w stringu znajdowały się cudzysłowia, należy użyć jednego typu cudzysłowów na zewnątrz i drugiego w środku:
```python
a = "Mój ulubiony film to 'Titanic'"
print(a)
> Mój ulubiony film to 'Titanic'

# lub
b = 'Mój ulubiony film to "Titanic"'
print(b)
> Mój ulubiony film to "Titanic"

# ale nie
c = "Mój ulubiony film to "Titanic""
print(c)
>    a = "Mój ulubiony film to "Titanic""
                                     ^
SyntaxError: invalid syntax
```

W ostatnim przypadku widzimy, że pojawia się błąd "SyntaxError" - błąd składni. W ten sposób Python mówi nam, że nie może wykonać danego polecenia, i podpowiada w którym miejscu jest błąd.

#### 4.3.2 Liczby w stringach
Uwaga! Liczby zapisane w cudzysłowach są traktowane jako stringi, nie jako liczby - nie można ich np. dodawać. Jeśli próbujemy to zrobić, dostaniemy błąd `TypeError`.
```python
a = "5"
b = 6
print(a+b)
> 
----> print(a+b)

TypeError: Can't convert 'int' object to str implicitly
```
#### 4.3.3 Operacje na stringach
Dodawanie
```python
a + b
a + " " + b
' '.join(a,b)
```


#### 4.3.3 Dodawanie stringów

Aby w stringu 
- indeksowanie
- slices
- split()





### 4.4 Nazywanie zmiennych

### 4.5 type()
Możemy sprawdzić typ zmiennej używając funkcji `type()`

```python
a = 5
b = 5.0
c = "5"
d = [5]

print(type(a))
> <class 'int'>
print(type(b))
> <class 'float'>
print(type(c))
> <class 'str'>
print(type(d))
> <class 'list'>
```


### 4.6 Zmiana typu zmiennych

## 5. input()

## 6. Listy

### 6.1 Tworzenie list
- indeksowanie
- ' '.join()

## Operacje na intach i floatach
| operacja | Znaczenie | Przykład|
| ------------- | ------------- | ------------- |
| +  | dodaj | `6.0 + 10` --> `16.0` |
| - | odejmij | `6.0 - 10` --> `4.0` |
| *  | pomnóż | `6.0 * 10` --> `60.0`|
| / | podziel | `6.0 / 10` --> `0.6`| 
| ** | podnieś do potęgi | `6.0 ** 10` --> `60466176.0` | 
| % | reszta z dzielenia | `10 % 6.0` --> `4.0` | 
| // | dzielenie do całości | `10 // 6.0` --> `1.0` | 


## Podsumowanie - ściąga 
| funkcja | Znaczenie | Przykład|
| ------------- | ------------- | ------------- |
| print()  | drukuj | `print(5)` |
| input()  | poproś użytkowniczkę o zmienną | `a = input("Podaj zmienną\n")`,  |
| split()  | podziel `string` | `a = "a,b,c,d"; a.split(',')` |
| join() | połącz elementy listy _zawierającej stringi_ w jeden `string` | `b = ['a','b', 'c']`; `','.join(b)` | 
| type() | sprawdź typ zmiennej | `type(a)` | 
| int() | zmień typ zmiennej na `int` | `int('5')` | 
| float() | zmień typ zmiennej na `float` | `float('5.0')` | 
| str() | zmień typ zmiennej na `string` | `str(1034)` | 
| bool() | zmień typ zmiennej na `bool` | `float(0)` | 

## pamiętajcie o:
- cudzysłowach w stringach 
  ```python
  print("cześć")
  #nie 
  # print(cześć)
  ```
- zmienne przychodzące z input() zawsze są stringami - jeśli chcecie używać ich jako intów lub floatów, użyjcie funkcji int() lub float()

  ```python
  wiek = input("Podaj wiek\n")
  rok_urodzenia = 2019 - int(wiek)
  ```
- można drukować na dwa sposoby: 
  - dodając kolejne zmienne po przecinku - wtedy nie musisz się przejmować zmianą wszystkich zmiennych na stringi. Funkcja dodaje też wtedy automatycznie spacje pomiędzy kolejnymi elementami.
  ```python
  wiek = 17
  print("Masz", wiek, "lat.")
  ```
  - tworząc nowy string znakiem `+` - wtedy wszystkie elementy dodawane muszą być stringiem, i trzeba pamiętać o spacjach:
  ```python
  wiek = 17
  print("Masz " +  str(wiek) + " lat.")
  ```


