# --- zadanie2 ---

#Wprowadzić jednym z powyższych sposobów tablicę danych ze strony https://en.wikipedia.org/wiki/Rough_set
#(chodzi o "Sample Information System" w sekcji "Example: equivalence-class structure").
#Wypisać rozmiary tej tablicy i nazwy kolumn. Za pomocą funkcji "iat" wyliczyć i wypisać sumy elementów
#w poszczególnych wierszach.

import numpy as np
import pandas as pd

sample_information_table = {
    'Object':['O1','O2','O3','O4','O5','O6','O7','08','O9','010'],
    'P1':[1,1,2,0,2,0,2,0,2,2],
    'P2':[2,2,0,0,1,0,0,1,1,0],
    'P3':[0,0,0,1,0,1,0,2,0,0],
    'P4':[1,1,1,2,2,2,1,2,2,1],
    'P5':[1,1,0,1,1,2,0,1,2,0]
}

data = pd.DataFrame(sample_information_table)
print(data)
print(data.shape)
noCol = data.shape[1]
noRow = data.shape[0]
print(f"Ilość kolumn w macierzy: {noCol}")
print(f"Ilość wierszy w macierzy: {noRow}")

sumy_wierszy = []
for i in range(noRow):
    suma = 0
    for j in range(1,noCol):
        suma += data.iat[i,j]
    sumy_wierszy.append(suma)

print(f"Sumy elementów w wierszach: {sumy_wierszy}")


