# Zajęcia 2
Na tych zajęciach nauczymy się wyrażeń logicznych i pętli w Pythonie.

## booleans (wartości zerojedynkowe)
Na poprzednich zajęciach wspomniałyśmy o `bool` (boolean, wartość zerojedynkowa) jako jednego z typu danych (inne typy to `int` (liczba naturalna, np. `-654`), `float` (liczba rzeczywista, zawiera `int`y, np. `4.3039`), `str` (string, słowo, jak `"hello"`)).

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
| is  | dwa obiekty mają to samo id | e is d |
| is not  | dwa obiekty mają inne id  | c is not d |



## if
wyrażenie `if` sprawdza czy warunek jest prawdziwy i:
- jeśli warunek jest prawdziwy (ma wartość `True`

if True:
	print("Prawda")

if False:
	print("Prawda")

Jezyk = “Python”

If jezyk == “Python”:
	print(“poprawny jezyk”)
If jezyk != “Python”:
	print(“niepoprawny jezyk”)


## if-else

## if-elif-else

## for

## while
