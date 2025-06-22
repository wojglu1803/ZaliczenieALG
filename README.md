"""
====================================================================================
                                  MathTool.GUI
====================================================================================

Opis projektu:
    MathTool.GUI to aplikacja desktopowa napisana w języku Python z wykorzystaniem 
    biblioteki Tkinter. Umożliwia użytkownikowi przeprowadzanie trzech operacji 
    matematycznych:
        - wyznaczanie liczb pierwszych (Sito Eratostenesa),
        - obliczanie wyznacznika macierzy kwadratowej (dowolnego rozmiaru),
        - szukanie miejsca zerowego wielomianu 5. stopnia metodą bisekcji.
    
    Aplikacja posiada prosty interfejs graficzny z oknami dialogowymi do wprowadzania 
    danych i prezentowania wyników.

------------------------------------------------------------------------------------
Wymagania:
    - System operacyjny: Windows 10/11, Linux lub macOS
    - Python: 3.10 lub nowszy
    - Edytor: Visual Studio Code (lub inny edytor obsługujący Pythona)
    - Biblioteki zewnętrzne:
        • numpy (do obliczania wyznacznika)
    
------------------------------------------------------------------------------------
Instalacja:
    1. Zainstaluj wymagane biblioteki:
        pip install numpy

    2. Uruchom aplikację:
        python main.py
       lub w Visual Studio Code:
        • Kliknij prawym przyciskiem na main.py → "Run Python File in Terminal"

------------------------------------------------------------------------------------
Funkcje aplikacji:

    1. Sito Eratostenesa:
        - Wprowadź liczbę całkowitą n
        - Zwraca listę liczb pierwszych ≤ n

    2. Wyznacznik macierzy:
        - Podaj rozmiar macierzy n
        - Wprowadź kolejne wiersze (liczby oddzielone spacją)
        - Wynik: wyznacznik macierzy obliczony z użyciem numpy

    3. Metoda bisekcji (wielomian 5. stopnia):
        - Wprowadź współczynniki a₀ do a₅ (łącznie 6 liczb)
        - Podaj przedział [a, b], w którym funkcja zmienia znak
        - Wynik: miejsce zerowe w zadanym przedziale

------------------------------------------------------------------------------------
Uwagi:
    • Funkcja wielomianowa musi zmieniać znak w przedziale (f(a) * f(b) < 0)
    • Działa na każdym systemie wspierającym tkinter i Pythona 3.10+
    • W razie potrzeby można rozbudować o:
        - zapis wyników do pliku,
        - wykresy funkcji,
        - analizę błędów i walidację danych.

------------------------------------------------------------------------------------
Licencja:
    Projekt udostępniany na licencji MIT – darmowy do użytku i modyfikacji.

====================================================================================
"""
