# --- zadanie2 ---

#Napisz program który odczytuje tablicę danych diabetes.csv (wszystkie wiersze i wszystkie kolumny).
#Następnie wykonuje szereg eksperymentów z tworzeniem klasyfikatorów i testowaniem ich metodą Cross-Validation,
#przy czym jest to zawsze klasyfikator k-NN (te same parametry tworzenia) występujący w powyższym przykładzie przy
#atrybucie decyzyjnym: 'decision'. Eksperymenty są wykonywane przy następującej liczbie zbiorów na które
#dzielony jest cały zbiór: 2, 3, 4, 5, 6, 7, 8, 9, 10 (chodzi o parametr cv).
#Wykonać wykres porównujący jakości klasyfikacji (accuracy) dla wszystkich eksperymemntów i wyciągnąć wniosek
#czy i jak parametr cv ma wpływ na jakośc klasyfikacji. Odpowiedni wniosek zapisać słownie
#w komentarzu na końcu komórki z rozwiązaniem.

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

dataset = pd.read_csv('../dane/diabetes.csv') #Odczytanie zbioru danych
noColumn = dataset.shape[1]

features = dataset.iloc[:,:noColumn-1]
labels = dataset.iloc[:,[noColumn-1]]

model = KNeighborsClassifier(n_neighbors=5,metric='euclidean')

#Liczba tzw. foldów (podziałów w teście CV)
noFold = [2, 3, 4, 5, 6, 7, 8, 9, 10]
accuracies = []

for fold in noFold:
    scores = cross_val_score(model, features, np.ravel(labels), cv=fold)
    print("Dokładnośc klasyfikacji (accuracy) dla części:",scores)
    print("Średnia dokładność:",scores.mean())
    print("Odchylenie standardowe:", scores.std())
    accuracies.append(scores.mean())

# Wykres porównujący dokładności klasyfikacji
plt.figure(figsize=(10, 6))
plt.plot(noFold, accuracies, marker='o')
plt.title('Dokładność klasyfikacji w zależności od liczby na którą dzielony jest zbiór')
plt.xlabel('Liczba na którą dzielony jest zbiór')
plt.ylabel('Dokładność klasyfikacji')
plt.grid(True)
plt.show()

#Wnioski: Parametr CV ma wpływ na dokładność klasyfikacji. Największa dokładność występuje dla dużej liczby podziałów, chociaż dla bardzo małej
#liczby również można zaobserwować dużą dokładność. 