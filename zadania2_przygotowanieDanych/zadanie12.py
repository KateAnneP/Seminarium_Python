# --- zadanie12 ---

#Napisz program który odczytuje tablicę danych nowotwory.csv i dokonuje na niej binaryzacji kolumn
#symbolicznych dla wszystkich kolumn oprócz ostatniej (czyli PRZY_ZG).
#Tablice po binaryzacji kolumn symbolicznych zapisujemy do pliku nowotwory_bin.csv.

import pandas as pd

dane = pd.read_csv('../dane/nowotwory.csv')
nazwy_kolumn = ['ROZPOZN','ZAAWREG','ZAAWPAT1','LECZENIE','RAD_CZYN1','WYNIKI']

dane2 = pd.get_dummies(dane, columns=nazwy_kolumn)

dane2.to_csv('nowotwory_bin.csv', index=False) #do csv