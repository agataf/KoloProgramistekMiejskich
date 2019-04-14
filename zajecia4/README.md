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

## 2. Powtórzenie funkcji
Ściągnij plik `funkcje.ipynb` powyżej. Możesz ściągnąć cały folder `do_pobrania.zip`, wyodrębnić pliki (klikając prawym klawiszem po ściągnięciu), i otworzyć plik `funkcje.ipynb` w opisany powyżej sposób.

## 3. Biblioteki

## 4. Wykresy

### 4.1 Zapisywanie stworzonych wykresów
- Stwórz wykres
- Nie zamykaj go! (nie używaj `plt.show()` ani `plt.close()`)
- Użyj funkcji `plt.savefig(<nazwa nowego pliku>`).
![Zapisz wykres](https://i.stack.imgur.com/m8HV9.png)
- Użyj `plt.show()`/`plt.close().

## 5. Praca z plikami

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
