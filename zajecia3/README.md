# Zajęcia 3

## 1. Powtórzenie wiadomości
Do tej pory przerobiłyśmy następujące zagadnienia:
- typy zmiennych w Pythonie
- listy
- używanie funkcji `input()` i `print()` do interakcji z użytkownikiem
- wartości zerojedynkowe `True` i `False`
- zdania warunkowe `if`, `if-else` i `if-elif-else`
- pętle `for` i `while`
- funkcję `range()`

## 2. break, continue, pass
`break`, `continue` i `pass` to trzy wyrażenia umożliwiające dokładniejszą kontrolę w pętlach `for` i `while`.

### 2.1 Break
Break (przewij) to wyrażenie bardzo przydatne w pętlach i zdaniach warunkowych. Pozwala ona na wyjście z pętli, w której właśnie jesteśmy

```python
for i in range(5):
  if i == 3:
    break
  print(i)
  
> 0 
1
2
```
## 2.2 Continue
Continue (kontynuuj) to wyrażenie pozwalające "przeskoczyć" do następnego kroku w pętli
```python
for i in range(5):
  if i == 3:
    continue
  print(i)
> 0 
1
2
4
```
## 2.3 Pass
Pass (przejdź) to oznaczenie "pustego" bloku kodu. W tym przypadku w warunku nie dzieje się nic.
```python
for i in range(5):
  if i == 3:
    pass
  print(i)
> 0 
1
2
3
4
```

## 3. Funkcje
Dotychczas na zajęciach używałyśmy wielu fukcji pythona - jak `print()`, `input()`, `split()`, `int()`, `str()`, `len()`, ect. (pełna lista znajduje się ![tutaj](https://github.com/agataf/KoloProgramistekMiejskich/blob/master/zajecia1/README.md#%C5%9Bci%C4%85ga).

Python pozwala nam też na tworzenie własnych funkcji.

Tak wygląda przykładowa funkcja mnożąca podaną liczbę przez 5
```python
def moja_funkcja(liczba): # przyjmij jeden argument
  wynik = liczba * 5
  return wynik # zwróć tą zmienną jako wynik funkcji
```

Możemy ją wywołać używając jej nazwy:
```python
a = 7
b = moja_funkcja(a)
print(b)
> 35
```
W tej funkcji "liczba" to argument, przyjmowany przez funkcję. Gdy wywołując funkcję, podajemy w nawiasie jakąś wartość (lub zmienną), wewnątrz funkcji przyjmuje ona nazwę wpisaną w definicji (w tym przypadku `a` przyjmuje nazwę `liczba` _ale tylko wewnątrz funkcji_).

W ostatniej linijce funkcji (`return wynik`), funkcja zwraca wartość, która zapisana zostanie w `b`, gdy ją wywołamy.

## 4. List comprehension
Jeżeli chcemy stworzyć listę stu pierwszych wielokrotności 5 używając pętli for:
```python
lista = []
for i in range(100):
  lista.append(i * 5)
```
Możemy to również zrobić używając jednej linijki:
```python
lista = [i * 5 for i in range(100)]
```
