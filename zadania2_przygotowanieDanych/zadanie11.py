# --- zadanie11 ---

#Dla danych z pliku rezygnacje.csv wykonać standaryzację następujących cech:
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
#Po wykonaniu standaryzacji tablicę zapisać do pliku rezygnacje_stand.csv

import pandas as pd
from sklearn.preprocessing import StandardScaler

dane = pd.read_csv('../dane/rezygnacje.csv')

scaler = StandardScaler()
lista_cech_do_standaryzacji = ['CZAS_POSIADANIA','L_WIAD_POCZTA_G','DZIEN_MIN','DZIEN_L_POL','DZIEN_OPLATA','WIECZOR_MIN','WIECZ_L_POL','WIECZ_OPLATA','NOC_MIN','NOC_L_POL','NOC_OPLATA','MIEDZY_MIN','MIEDZY_L_POL','MIEDZY_OPLATA','L_POL_BIURO','REZYGN'] #wybranie cech do przeskalowania

dane[lista_cech_do_standaryzacji] = scaler.fit_transform(dane[lista_cech_do_standaryzacji]) #Wykonanie standaryzacji

print("Dane po standaryzacji:")
print(dane.head(10))

dane.to_csv('rezygnacje_stand.csv', index=False) #do csv