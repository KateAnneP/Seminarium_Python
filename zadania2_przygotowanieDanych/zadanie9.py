# --- zadanie9 ---

#Napisz program który odczytuje tablicę danych rezygnacje.csv, wybiera z niej kolumny:
#CZAS_POSIADANIA, PLAN_MIEDZY, POCZTA_G, L_WIAD_POCZTA_G, L_POL_BIURO, REZYGN.
#Następnie w wybranej podtablicy w kolumnie REZYGN wymienia wartość 1 na 'TAK', a wartość 0 na 'NIE'.
#Wybraną podtablicę zapisujemy do pliku rezygnacje_TAK_NIE.csv. Wypisz 5 pierwszych i 5 ostatnich wierszy tej
#podtablicy.

import pandas as pd

dane = pd.read_csv('../dane/rezygnacje.csv')

kolumny = ['CZAS_POSIADANIA', 'PLAN_MIEDZY', 'POCZTA_G', 'L_WIAD_POCZTA_G', 'L_POL_BIURO', 'REZYGN']
rezygnacje_sel = dane[kolumny]

dane['REZYGN'] = dane['REZYGN'].replace(1, 'TAK')
dane['REZYGN'] = dane['REZYGN'].replace(0, 'NIE')


dane.to_csv('rezygnacje_TAK_NIE.csv', index=False) #do csv

print("Pierwsze 5 wierszy:")
print(dane.head())
print("Ostatnie 5 wierszy:")
print(dane.tail())