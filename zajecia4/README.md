# Zajęcia 4

## 1. Jupyter notebook
### 1.1 Ściągnij Anacondę - program zawierający Pythona oraz biblioteki Pythona, których będziemy używać
- zwróć uwagę na wersję Pythona (3.7 na tym kursie)
- zwróć uwagę na wersję Anacondy (na Maca lub Windowsa)
https://www.anaconda.com/distribution/#download-section

### 1.2 Otwórz Jupyter notebook
w Windowsie: 
- po zainstalowaniu Anacondy znajdź program Anaconda Navigator
![Anaconda Navigator](https://cdn-images-1.medium.com/max/2400/1*8VwF5RUh4vEf4FfrKMw7qg.png)
- otwórz Jupyter notebook

w Macu:
- po zainstalowaniu Anacondy znajdź program Terminal
- w Terminalu wpisz `jupyter notebook`
- okno Jupyter notebook otworzy się w twojej przeglądarce

### 1.3 Używanie Jupyter notebook
![Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/_images/dashboard_files_tab.png)
- Pierwszą widoczną stroną jest przeglądarka plików. Znajduje się ona na poziomie Home (ponad Desktop, Downloads).
- Żeby otworzyć ściągnięty plik, znajdź folder, w którym się znajduje (np. klikając Dowloads lub Documents)
- Żeby stworzyć nowy plik, kliknij "New" po prawej stronie, i wybierz "Python"
![Nowy plik](https://jupyter-notebook.readthedocs.io/en/stable/_images/dashboard_files_tab_new.png)


## Praca na zajęciach
Na te zajęcia przygotowałam Jupyter Notebooks do wypełnienia przez Was (wypełnione notebooki znajdują się w folderze `rozwiązania`). Możesz ściągnąć cały folder `do_pobrania.zip`, wyodrębnić pliki (klikając prawym klawiszem po ściągnięciu), i otworzyć plik `funkcje.ipynb` w opisany powyżej sposób.

## 2. Powtórzenie funkcji

Zadanie - plik `funkcje.ipynb`

## 3. Biblioteki

Zadanie - plik `biblioteki.ipynb`

Biblioteki w Pythonie to zbiory funkcji napisanych przez inne osoby, których możemy używać bez konieczności implementowania rozwiązań samym. Aby użyć biblioteki (np. biblioteki `math`), należy ją najpierw zaimportować, pisząc
```
import math
```
Kiedy chcemy użyć jakiejś funkcji z biblioteki, używamy formy `<nazwa biblioteki>.<nazwa funkcji>(<argumenty funkcji>)`, na przykład:
```
a = math.pow(2,8) # funkcja pow podnosi pierwszy argument do potęgi podanej w drugim argumencie
print(a)
> 256.0
```
Dokumentację dotyczącą konkretnych funkcji możemy bez problemu znaleźć w internecie, wpisując w google zapytania typu "python math library function power".

Biblioteki, których będziemy używać na tych zajęciach, to
- math (podstawowa biblioteka do działań matematycznych)
- random (biblioteka do generowania liczb losowych)
- pyplot (biblioteka do rysowania wykresów)
- pandas (biblioteka do operacji na tabelach danych)

Aby poznać bibliotekę, warto czasem przerobić tutoriale publikowane na stronie twórców bibliotek:
- [Tutorial Pyplot](https://matplotlib.org/users/pyplot_tutorial.html)
- [Tutorial Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#min)
- [Inny tutorial Pandas](https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/)

```
import math
import random
import matplotlib.pyplot as plt
import pandas as pd
```

## 4. Wykresy

Zadanie - plik `wykresy-wprowadzenie.ipynb`

### 4.1 Zapisywanie stworzonych wykresów
- Stwórz wykres
- Nie zamykaj go! (nie używaj `plt.show()` ani `plt.close()`)
- Użyj funkcji `plt.savefig(<nazwa nowego pliku>`).
![Zapisz wykres](https://i.stack.imgur.com/m8HV9.png)
- Użyj `plt.show()`/`plt.close()`.

## 5. Praca z plikami

Zadanie - plik `zajecia-wykresy.ipynb`

### 5.1 Ładowanie pliku csv do zmiennej:

Ściągnij plik `heart-disease-uci.zip` i odpakuj go - powinnaś otrzymać plik `heart.csv` (dostępny również tutaj: https://www.kaggle.com/ronitf/heart-disease-uci). Znajdź ścieżkę do pliku i skopiuj go. Zakładając że plik zostaje zapisany w folderze Downloads, załaduj go używając polecenia:

- na Windowsie
```
import pandas as pd
heart_data = pd.read_csv('C:/Users/<username>/Downloads/heart.csv')
```
- na Macu
```
import pandas as pd
heart_data = pd.read_csv('/Users/<username>/Downloads/heart.csv')
```

Uwaga: ścieżka nie powinna zawierać spacji (nazwy folderów nie mogą ich mieć). Czasem przy kopiowaniu zapisywany jest dziwny format liter - warto wkleić i wyciąć ścieżkę w okienku w google, co usunie formatowanie.
