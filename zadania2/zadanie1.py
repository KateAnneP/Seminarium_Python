# --- zadanie 1 ---

#Napisać program, który  pyta o liczbę wierszy i kolumn macierzy kwadratowej, tworzy taką
#macierz, odczytuje z klawiatury elementy tej macierzy  (czytanie wierszami) oraz oblicza i wypisuje:
#- sumę elementów leżących nad główną przekatną,
#- minimalny element na głównej przekątnej,
#- wyznacznik tej macierzy - patrz: https://pl.wikipedia.org/wiki/Rozwini%C4%99cie_Laplace%E2%80%99a

import numpy as np

n = int(input("Podaj liczbę kolumn/wierszy: "))

el_macierzy = []

for i in range(0,n):
    wiersz = []
    for j in range(0,n):
        element = int(input("Podaj kolejny element macierzy: "))
        wiersz.append(element)
    el_macierzy.append(wiersz)

macierz = np.array(el_macierzy)
print(macierz)

suma = 0
min_element = macierz[0,0]
for i in range(n):
    for j in range(n):
        if j>i:
            suma += macierz[i,j]
        if i == j and macierz[i,j] < min_element:
            min_element = macierz[i,j]

print(f"Suma elementów leżących powyżej przekątnej macierzy wynosi: {suma}")
print(f"Minimalny element na przekątnej to {min_element}")

#wyznacznik
def minor(macierz, i, j):
    return np.delete(np.delete(macierz, i, axis=0), j, axis=1)

def determinant(macierz):
    n = macierz.shape[0]
    if n == 1:
        return macierz[0, 0]
    else:
        det = 0
        for j in range(n):
            det += (-1) ** j * macierz[0, j] * determinant(minor(macierz, 0, j))
        return det

det = determinant(macierz)
print("Wyznacznik macierzy:", det)

