# --- zadanie3 ---

#Napisz program który odczytuje tablicę danych rezygnacje.csv oraz wybiera z niej wszystkie wiersze oraz
#kolumny: CZAS_POSIADANIA, PLAN_MIEDZY, POCZTA_G, L_WIAD_POCZTA_G, L_POL_BIURO, REZYGN.
#Następnie wykonuje eksperyment, którego celem jest wygenerowanie wartości decyzji dla obiektów testowych
#z pliku czy_zrezygnuja.csv. Klasyfikator jest tworzony dla tablicy rezygnacje.csv metodą k-NN z użyciem tych samych
#parametrów tworzenia jak w powyższym przykładzie i przy atrybucie decyzyjnym 'REZYGN'.
#Wygenerowane decyzję są dopisywane jako ostatnia kolumna do zbioru odczytanego z pliku czy_zrezygnuja.csv,
#po czym zmodyfikowany zbiór danych (z dodaną kolumną) jest zapisywany do pliku czy_zrezygnuja_dec.csv.
#UWAGA: W danych z pliku czy_zrezygnuja.csv nie ma atrybutu decyzyjnego.

import numpy as np
import pandas as pd
from sklearn import metrics, datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

dataset = pd.read_csv('../dane/rezygnacje.csv')
dataset_test = pd.read_csv('../dane/czy_zrezygnuja.csv')
kolumny = ['CZAS_POSIADANIA','PLAN_MIEDZY', 'POCZTA_G', 'L_WIAD_POCZTA_G','L_POL_BIURO','REZYGN']
datasetTrain = dataset[kolumny]

kolumny2 = ['CZAS_POSIADANIA','PLAN_MIEDZY', 'POCZTA_G', 'L_WIAD_POCZTA_G','L_POL_BIURO']
datasetTest = dataset_test[kolumny2]

noColumn = datasetTrain.shape[1]

features_train = datasetTrain.iloc[:,:noColumn-1] #Część warunkowa tablicy treningowej
labels_train = datasetTrain.iloc[:,[noColumn-1]] #Kolumna decyzyjna tablicy treningowej

features_test = datasetTest.loc[:, kolumny2[:-1]] #Część warunkowa tablicy testowej

model = KNeighborsClassifier(n_neighbors=3,metric='euclidean')
model.fit(features_train, np.ravel(labels_train)) #Uczenie klasyfikatora

labels_predicted = model.predict(features_test) #Testowanie tablicy testowej

# Dodanie przewidywanych wartości jako nowa kolumna do zbioru testowego
datasetTest['REZYGN'] = labels_predicted

# Zapisanie zmodyfikowanego zbioru danych do nowego pliku CSV
datasetTest.to_csv('../dane/czy_zrezygnuja_dec.csv', index=False)