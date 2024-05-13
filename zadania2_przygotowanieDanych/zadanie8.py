# --- zadanie8 ---

#Napisz program który odczytuje tablicę danych rezygnacje.csv, wybiera z niej kolumny:
#CZAS_POSIADANIA, PLAN_MIEDZY, POCZTA_G, L_WIAD_POCZTA_G, L_POL_BIURO, REZYGN. Ponadto, wybiera tych
#klientów, którzy mają plan miedzynarodowy (PLAN_MIEDZY=1), ale nie mają poczty głosowej (POCZTA_G=0) oraz dzwonili
#przynajmniej raz do biura obsługi klienta (L_POL_BIURO>0) .
#Wybraną podtablicę zapisujemy do pliku rezygnacje_sel2.csv. Wypisz 5 pierwszych i 5 ostatnich wierszy tej podtablicy.

import pandas as pd

dane = pd.read_csv('../dane/rezygnacje.csv')

kolumny = ['CZAS_POSIADANIA', 'PLAN_MIEDZY', 'POCZTA_G', 'L_WIAD_POCZTA_G', 'L_POL_BIURO', 'REZYGN']
rezygnacje_sel = dane[kolumny]

rezygnacje_sel2 = rezygnacje_sel[(rezygnacje_sel['PLAN_MIEDZY'] == 1) & (rezygnacje_sel['POCZTA_G'] == 0) & (rezygnacje_sel['L_POL_BIURO'] > 0)]

rezygnacje_sel2.to_csv('rezygnacje_sel2.csv', index=False) #do csv

print("Pierwsze 5 wierszy:")
print(rezygnacje_sel2.head())
print("Ostatnie 5 wierszy:")
print(rezygnacje_sel2.tail())
