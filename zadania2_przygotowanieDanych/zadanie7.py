# --- zadanie7 ---

#Napisz program który odczytuje tablicę danych rezygnacje.csv, wybiera z niej wszystkie wiersze i kolumny:
#CZAS_POSIADANIA, #PLAN_MIEDZY, POCZTA_G, L_WIAD_POCZTA_G, L_POL_BIURO, REZYGN, oraz zapisuje nową tablicę
#danych (z wybranymi kolumnami) do pliku rezygnacje_sel.csv. Wypisz 5 pierwszych i 5 ostatnich wierszy
#nowej tablicy danych. Zapisz tablicę także do pliku binarnego rezygnacje_sel.bin.

import pandas as pd

dane = pd.read_csv('../dane/rezygnacje.csv')

kolumny = ['CZAS_POSIADANIA', 'PLAN_MIEDZY', 'POCZTA_G', 'L_WIAD_POCZTA_G', 'L_POL_BIURO', 'REZYGN']
rezygnacje_sel = dane[kolumny]

rezygnacje_sel.to_csv('rezygnacje_sel.csv', index=False) #do csv

print("Pierwsze 5 wierszy:")
print(rezygnacje_sel.head())
print("Ostatnie 5 wierszy:")
print(rezygnacje_sel.tail())

rezygnacje_sel.to_pickle('rezygnacje_sel.bin') #do binarnego