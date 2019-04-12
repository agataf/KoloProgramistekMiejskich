# Zajęcia 2

## 1. Repl.it

## 2. Twój pierwszy program
```
print(“Hello World!”)
> Hello World!
```
cudzysłowia są bardzo ważne! Jeśli spróbujemy zrobić to samo bez cudzysłowia, program zwróci nam błąd `invalid syntax` (niepoprawna składnia)

```
print(Hello World!)

>  File "<ipython-input-46-734633aabfd1>", line 1
    print(Hello World!)
                    ^
SyntaxError: invalid syntax
```
## 3. Komentarze
```
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

### 4.1 type()

### 4.1 Stringi 

- indeksowanie
- slices
- split()


### 4.2 Int

### 4.3 Float

### 4.4 Nazywanie zmiennych

### 4.5 Zmiana typu zmiennych

## 5. input()

## 6. Listy

### 6.1 Tworzenie list
- indeksowanie
- ' '.join()

## %, //, /, +, -,

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
- cudzysłowiach w stringach 
  ```
  print("cześć")
  #nie 
  # print(cześć)
  ```
- zmienne przychodzące z input() zawsze są stringami - jeśli chcecie używać ich jako intów lub floatów, użyjcie funkcji int() lub float()

  ```
  wiek = input("Podaj wiek\n")
  rok_urodzenia = 2019 - int(wiek)
  ```
- można drukować na dwa sposoby: 
  - dodając kolejne zmienne po przecinku - wtedy nie musisz się przejmować zmianą wszystkich zmiennych na stringi. Funkcja dodaje też wtedy automatycznie spacje pomiędzy kolejnymi elementami.
  ```
  wiek = 17
  print("Masz", wiek, "lat.")
  ```
  - tworząc nowy string znakiem `+` - wtedy wszystkie elementy dodawane muszą być stringiem, i trzeba pamiętać o spacjach:
  ```
  wiek = 17
  print("Masz " +  str(wiek) + " lat.")
  ```


