## POZIOM ŁATWIEJSZY

### 1. Dodatnie (IF)
Napisz program, który prosi użytkowniczkę o podanie liczby, i jeśli jest dodatnia, odpowiada "to jest liczba dodatnia". W przeciwnym wypadku nie odpowiada nic.
```
Podaj liczbę
> 782
Ta liczba jest dodatnia

Podaj liczbę
> -8

```

### 2. Zajęcia (IF)
Napisz program, który pyta użytkowniczkę o dzień tygodnia, a następnie jeśli jest środa, odpowiada "dzisiaj są zajęcia". W przeciwnym wypadku nie odpowiada nic.

```
Podaj dzień tygodnia
> Środa
Dzisiaj są zajęcia.

Podaj dzień tygodnia
> Poniedziałek

```

### 3. Dodatnie czy ujemne? (IF-ELSE)
Napisz program, który prosi użytkowniczkę o podanie liczby, a następnie mówi czy liczba ta jest dodatnia czy ujemna (załóż że 0 jest liczbą dodatnią)
```
Podaj liczbę
> -8
Ta liczba jest ujemna

Podaj liczbę
> 782
Ta liczba jest dodatnia
```

### 4. Zajęcia (IF-ELSE)
Napisz program, który pyta użytkowniczkę o dzień tygodnia, a następnie
- jeśli jest środa, odpowiada "dzisiaj są zajęcia"
- jeśli jest inny dzień odpowiada, pisze "dzisiaj nie ma zajęć"
```
Podaj dzień tygodnia
> Poniedziałek
Dzisiaj nie ma zajęć.
```

### 5. Menu (IF-ELIF-ELSE)
Napisz program, który pyta użytkowniczkę o dzień tygodnia, a następnie podaje menu na dany dzień. Każdego dnia menu jest inne: Poniedziałek - pizza. Wtorek - pierogi. Środa - gniocci. Czwartek - ryba. Piątek - spaghetti.
```
Podaj dzień tygodnia
> Środa
Dzisiaj podajemy gniocci.
```

### 6. Trójkąt (FOR)
Poproś użytkowniczkę o liczbę i wydrukuj trójkąt o podanej wysokości.

```
Podaj liczbę
> 5
*
* *
* * *
* * * *
* * * * *
```

### 7. Trójkąt 2 (WHILE)
Wykonaj powyższe zadanie, używając pętli WHILE.

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

## POZIOM TRUDNIEJSZY
### 1. Rzut kośćmi. 

Przyjmij k1 i k2 jako liczba wyrzuconych oczek.

Sprawdź, czy podane wartości są w odpowiednim zakresie wartości (od 1 to 6).

Jeśli nie, wydrukuj odpowiedni komunikat (np. "wartość 7 jest niepoprawna").

Jeżeli zakres jest poprawny, podaj wynik według następującego klucza:

- jeśli suma to 7 lub 11, wydrukuj "wygrana"
- jeśli suma to 2, 3, lub 12, wydrukuj "przegrana"
- w innym wypadku wydrukuj liczbę oczek.

### 2. Suma

Użyj pętli for, by znaleźć elementy o wartości powyżej 30 w liście oraz oblicz ich sumę.
```
lista = [10, 40, 56, 23, 56, 1]
```

### 3. Trójkąt
Poproś użytkowniczkę o liczbę i wydrukuj trójkąt o podanej wysokości.

```
Podaj liczbę
> 5
*
* *
* * *
* * * *
* * * * *
```

### 4. Ulubione
Używając pętli FOR, zapytaj użytkowniczkę o pięć ulubionych zespołów. Każdy z nich dodaj do listy "ulubione" używając funkcji `append()`. Wydrukuj zespoły od tyłu, używając pętli FOR.

### 5. Mnożenie
Poproś użytkowniczkę o 5 liczb, a następnie podaj wynik ich mnożenia. Użyj nie więcej niż 7 linii.

### 6. Wiek (WHILE)
Zapytaj użytkowniczkę jak na na imię, i ile ma lat i wydrukuj komunikat.

jeśli użytkowniczka poda błędną odpowiedź na którekolwiek z pytań (wiek nie będzie liczbą, lub odpowiedź nie będzie brzmiała tak/nie), użyj pętli while, dopóki nie dostaniesz poprawnej odpowiedzi.

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