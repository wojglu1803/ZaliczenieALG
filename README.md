# ZaliczenieALG
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
  Klonowanie lub utworzenie pliku:
    Utwórz folder projektu i w nim plik main.py. Skopiuj do niego kod źródłowy aplikacji.
  Instalacja wymaganych bibliotek:
  W terminalu:
    pip install numpy
  Uruchomienie aplikacji:
  Z poziomu terminala VS Code:
    python main.py
    Alternatywnie: kliknij prawym przyciskiem myszy w main.py → Run Python File in Terminal

Funkcje aplikacji
  Strona główna:
    Po uruchomieniu pojawia się okno z trzema przyciskami umożliwiającymi wybór funkcji matematycznej do wykonania:
  Sito Eratostenesa
    Wprowadź liczbę całkowitą n
    Wynikiem jest lista wszystkich liczb pierwszych ≤ n
  Wyznacznik macierzy
    Podaj rozmiar macierzy n
    Wprowadź po kolei każdy wiersz (oddzielając liczby spacją)
    Wynik: wyznacznik obliczony z wykorzystaniem biblioteki numpy
  Metoda bisekcji (wielomian 5. stopnia)
    Wprowadź 6 współczynników wielomianu w kolejności od a₀ do a₅ (czyli: a0 a1 a2 a3 a4 a5)
    Wprowadź przedział [a, b], w którym funkcja zmienia znak
    Wynik: przybliżona wartość miejsca zerowego

