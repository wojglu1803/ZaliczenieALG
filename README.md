# ZaliczenieALG
MathTool.GUI
Opis projektu:
MathTool.GUI to aplikacja desktopowa napisana w języku Python z wykorzystaniem biblioteki Tkinter. Umożliwia użytkownikowi przeprowadzanie trzech niezależnych operacji matematycznych:

wyznaczanie liczb pierwszych przy użyciu algorytmu Sita Eratostenesa,

obliczanie wyznacznika macierzy kwadratowej (dowolnego rozmiaru),

szukanie miejsca zerowego wielomianu 5. stopnia metodą bisekcji.

Projekt posiada prosty i intuicyjny interfejs graficzny, który pozwala użytkownikowi wprowadzić dane wejściowe i natychmiast uzyskać wynik w formie okna dialogowego.

Wymagania
System operacyjny: Windows 10 / 11, Linux, macOS

Środowisko programistyczne: Visual Studio Code lub dowolny edytor Python

Wersja Pythona: Python 3.10 lub nowszy

Biblioteki zewnętrzne:

numpy – do obliczania wyznacznika

Instalacja i uruchomienie
1. Klonowanie lub utworzenie pliku:
Utwórz folder projektu i w nim plik main.py. Skopiuj do niego kod źródłowy aplikacji.

2. Instalacja wymaganych bibliotek:
W terminalu:

bash
Kopiuj
Edytuj
pip install numpy
3. Uruchomienie aplikacji:
Z poziomu terminala VS Code:

bash
Kopiuj
Edytuj
python main.py
Alternatywnie: kliknij prawym przyciskiem myszy w main.py → Run Python File in Terminal

Funkcje aplikacji
Strona główna:
Po uruchomieniu pojawia się okno z trzema przyciskami umożliwiającymi wybór funkcji matematycznej do wykonania:

1. Sito Eratostenesa
Wprowadź liczbę całkowitą n

Wynikiem jest lista wszystkich liczb pierwszych ≤ n

2. Wyznacznik macierzy
Podaj rozmiar macierzy n

Wprowadź po kolei każdy wiersz (oddzielając liczby spacją)

Wynik: wyznacznik obliczony z wykorzystaniem biblioteki numpy

3. Metoda bisekcji (wielomian 5. stopnia)
Wprowadź 6 współczynników wielomianu w kolejności od a₀ do a₅ (czyli: a0 a1 a2 a3 a4 a5)

Wprowadź przedział [a, b], w którym funkcja zmienia znak

Wynik: przybliżona wartość miejsca zerowego

Dodatkowe informacje
Dla działania metody bisekcji, funkcja musi zmieniać znak w zadanym przedziale (f(a) * f(b) < 0)

Interfejs działa w każdym systemie operacyjnym wspierającym Tkinter
