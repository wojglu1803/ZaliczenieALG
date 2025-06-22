import tkinter as tk
from tkinter import messagebox, simpledialog
import numpy as np

# === ALGORYTM SITA ERATOSTENESA ===
def sito_eratostenesa(n):
    if n < 2:
        return []
    sito = [True] * (n + 1)
    sito[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sito[i]:
            for j in range(i*i, n+1, i):
                sito[j] = False
    return [i for i, is_prime in enumerate(sito) if is_prime]

# === WYZNACZNIK MACIERZY ===
def wyznacznik_macierzy(macierz):
    try:
        return np.linalg.det(np.array(macierz))
    except Exception as e:
        return str(e)

# === METODA BISEKCJI ===
def wartosc_wielomianu(wsp, x):
    return sum(c * (x ** i) for i, c in enumerate(wsp))

def bisekcja(wsp, a, b, tol=1e-6, max_iter=100):
    fa = wartosc_wielomianu(wsp, a)
    fb = wartosc_wielomianu(wsp, b)
    if fa * fb > 0:
        return "Brak zmiany znaku – brak miejsca zerowego w przedziale."

    for _ in range(max_iter):
        c = (a + b) / 2
        fc = wartosc_wielomianu(wsp, c)
        if abs(fc) < tol or (b - a) / 2 < tol:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return c

# === GUI ===
def uruchom_sito():
    n = simpledialog.askinteger("Sito Eratostenesa", "Podaj liczbę całkowitą n:")
    if n is not None:
        liczby_pierwsze = sito_eratostenesa(n)
        messagebox.showinfo("Wynik", f"Liczby pierwsze do {n}:\n{liczby_pierwsze}")

def uruchom_wyznacznik():
    size = simpledialog.askinteger("Wyznacznik", "Podaj rozmiar macierzy kwadratowej (np. 3):")
    if size is not None:
        macierz = []
        for i in range(size):
            wiersz = simpledialog.askstring("Macierz", f"Podaj wiersz {i+1} (oddzielone spacjami):")
            try:
                macierz.append([float(x) for x in wiersz.strip().split()])
            except:
                messagebox.showerror("Błąd", "Nieprawidłowe dane!")
                return
        if any(len(w) != size for w in macierz):
            messagebox.showerror("Błąd", "Macierz nie jest kwadratowa!")
            return
        wynik = wyznacznik_macierzy(macierz)
        messagebox.showinfo("Wyznacznik", f"Wyznacznik = {wynik:.4f}")

def uruchom_bisekcja():
    wsp_str = simpledialog.askstring("Wielomian", "Podaj 6 współczynników (a0 a1 a2 ... a5):")
    przedzial_str = simpledialog.askstring("Przedział", "Podaj przedział (a b):")
    try:
        wsp = [float(x) for x in wsp_str.strip().split()]
        a, b = [float(x) for x in przedzial_str.strip().split()]
        if len(wsp) != 6:
            raise ValueError
        wynik = bisekcja(wsp, a, b)
        messagebox.showinfo("Miejsce zerowe", f"Wynik: {wynik}")
    except:
        messagebox.showerror("Błąd", "Nieprawidłowe dane!")

# === GŁÓWNE OKNO ===
root = tk.Tk()
root.title("Aplikacja Matematyczna")
root.geometry("300x250")

tk.Label(root, text="Wybierz opcję:", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Sito Eratostenesa", width=25, command=uruchom_sito).pack(pady=5)
tk.Button(root, text="Wyznacznik macierzy", width=25, command=uruchom_wyznacznik).pack(pady=5)
tk.Button(root, text="Metoda bisekcji", width=25, command=uruchom_bisekcja).pack(pady=5)
tk.Button(root, text="Zamknij", width=25, command=root.destroy).pack(pady=20)

root.mainloop()
