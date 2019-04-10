### 1. Kalkulator
Stwórz program-kalkulator, który będzie traktował znak ^ jako znak potęgi (w python potęga to **).
```
Podaj działanie
>2^3
8
>2^-1
0.5
```

### 2. Trójkąt
Poproś użytkowniczkę o liczbę i wydrukuj choinkę o podanej wysokości.
a. używając symbolu mnożenia w pętli
b. używając funkcji `append` i `join`

```
Podaj liczbę
> 5
*
- *
- - *
- - - *
- - - - *
```

### 3. Błędy
Zmień poniższy kod tak, aby prosił użytkowniczkę o liczbę oczek aż nie poda ona poprawnego typu danych (cyfry).

```
k1 = input(“podaj liczbę oczek”)

try:
    int(k1)
except:
    print(“liczba musi być cyfrą”)
```

### 4. Suma-mnożenie
Dla podanej listy b, policz następujące działanie używając pętli: b[0] * 1 + b[1] * 2 + b[2] * 3 + b[3] * 4.
```
b = [2, 6, 3, 2, 6]
```
### 5. Imię
Stwórz funkcję, która pyta przyjmuje jeden argument - imię użytkowniczki, a następnie ją wita
```
funkcja_witania("Ania")
> Cześć Ania
```


### 6. Choinka
Stwórz funkcję, która drukuje choinkę
```
choinka(3)
>
*
- *
- - *
```

### 7. Rewers
Stwórz funkcję, która przyjmuje listę i zwraca jej odwrotność (reverse)
```
naodwrot([4,5,6,7])
> [7,6,5,4]
```

### 8. Suma-mnożenie w funkcji
Stwórz funkcję, która wykonuje działanie podane w zadaniu 4, ale dla dowolnej listy
```
dodaj_mnoz([1,2,3,4])
> 30
```

### (*) 9. Choinka w stringu
Stwórz funkcję `choinka` która nie drukuje choinki, tylko zwraca string w którym jest choinka
```
narysowane = choinka(5)
print(narysowane)
>
>
*
- *
- - *
- - - *
- - - - *
```




