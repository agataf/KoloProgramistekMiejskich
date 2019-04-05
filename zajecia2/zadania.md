# Zajęcia 2

## if, if-else, if-elif-else
### 1. Hasło

Zdefiniuj swoje hasło (np. `haslo = 3729`). Zapytaj użytkowniczkę o hasło. Jeśli zna poprawne hasło, pozwól jej wejść. Jeśli nie zna, powiedz że hasło jest błędne.
```
Podaj PIN
> 2880
To hasło jest błędne.

Podaj PIN
> 3729
Pin poprawny! Możesz wejść.
```

### 2. Pełnoletniość

Zapytaj użytkowniczkę o wiek. Podaj odpowiedź "Jesteś małoletnia/Jesteś niepełnoletnia/Jesteś pełnoletnia" w zależności od jej wieku (do 13, do 18 lub powyżej 18 lat).
```
Ile masz lat?
> 17
Jesteś niepełnoletnia.

Ile masz lat?
> 10
Jesteś małoletnia.
```
Podpowiedź: przyda się tutaj forma if-elif-else

### 3. Wiek
Zauważ że po samym roku nie można podać dokładnego wieku. Jeśli ktoś ma urodziny np. w sierpniu, błędnie założymy, że ma już tyle lat, ile wynikałoby z roku urodzenia.

Zapytaj użytkowniczkę jak na na imię, i ile ma lat i wydrukuj komunikat:
```
Jak masz na imię?
> Ania
Ile masz lat?
> 32
Czy miałaś już urodziny w tym roku? (tak/nie)
> nie
Ania, urodziłaś się w 1986 roku.
```

## for, range
### 1. Kwadraty
Używając pętli for, wydrukuj kwadraty wszystkich liczb od 0 do 10.

Podpowiedź: użyj funkcji `range()`.

### 2. Liczby parzyste
Używając pętli for, stwórz nową listę zawierającą jedynie parzyste elementy listy `liczby`:
```
liczby = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
```
Źródło: https://www.learnpython.org/en/Loops


## while
### 1. Hasło
Zapytaj użytkowniczkę o hasło. Jeśli zna poprawne hasło, pozwól jej wejść. Jeśli nie zna, zapytaj o nie ponownie.
```
Podaj PIN
> 2880
To hasło jest błędne, spróbuj ponownie.

Podaj PIN
> 3729
Pin poprawny! Możesz wejść.
```

### 2. Wiek

Zapytaj użytkowniczkę jak na na imię, i ile ma lat i wydrukuj komunikat:
```
Jak masz na imię?
> Ania
Ile masz lat?
> 32
Czy miałaś już urodziny w tym roku? (tak/nie)
> jhhf
To jest błędna odpowiedź. Podaj odpowiedź tak lub nie.
Czy miałaś już urodziny w tym roku? (tak/nie)
> nie
Ania, urodziłaś się w 1986 roku.
```


