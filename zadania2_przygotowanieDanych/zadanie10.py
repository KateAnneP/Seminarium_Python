# --- zadanie10 ---

#Dla danych z pliku rezygnacje.csv wykonać skalowanie następujących cech:
#CZAS_POSIADANIA,
#L_WIAD_POCZTA_G,
#DZIEN_MIN,
#DZIEN_L_POL,
#DZIEN_OPLATA,
#WIECZOR_MIN,
#WIECZ_L_POL,
#WIECZ_OPLATA,
#NOC_MIN,
#NOC_L_POL,
#NOC_OPLATA,
#MIEDZY_MIN,
#MIEDZY_L_POL,
#MIEDZY_OPLATA,
#L_POL_BIURO,REZYGN
#
#Po wykonaniu skalowania tablicę zapisac do pliku rezygnacje_skal.csv

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

dane = pd.read_csv('../dane/rezygnacje.csv')

scaler = MinMaxScaler()
lista_cech_do_przeskalowania = ['CZAS_POSIADANIA','L_WIAD_POCZTA_G','DZIEN_MIN','DZIEN_L_POL','DZIEN_OPLATA','WIECZOR_MIN','WIECZ_L_POL','WIECZ_OPLATA','NOC_MIN','NOC_L_POL','NOC_OPLATA','MIEDZY_MIN','MIEDZY_L_POL','MIEDZY_OPLATA','L_POL_BIURO','REZYGN'] #wybranie cech do przeskalowania

dane[lista_cech_do_przeskalowania] = scaler.fit_transform(dane[lista_cech_do_przeskalowania]) #Wykonanie skalowania

print("Dane przeskalowane:")
print(dane.head(10))

dane.to_csv('rezygnacje_skal.csv', index=False) #do csv


