# --- zadanie1 ---

#Napisz program który odczytuje tablicę danych rezygnacje.csv oraz wybiera z niej wszystkie wiersze oraz
#kolumny: CZAS_POSIADANIA, PLAN_MIEDZY, POCZTA_G, L_WIAD_POCZTA_G, L_POL_BIURO, REZYGN.
#Następnie wykonuje szereg eksperymentów z tworzeniem klasyfikatorów i testowaniem ich metodą Train&Test, przy czym
#jest to zawsze klasyfikator k-NN (te same parametry tworzenia) występujący w powyższych 2 przykładach przy
#atrybucie decyzyjnym 'REZYGN'. Eksperymenty są wykonywane przy następującyh wielkościach tablicy
#treningowej: 90%, 80%, 70%, 60%, 50%, 40%, 30%, 20% i 10%.
#Oczywiście, jeśli np. tablica treningowa liczy 70% całych danych, to tablica testowa liczy 100% - 70% = 30%.
#Wykonać wykres porównujący jakości klasyfikacji (accuracy) dla wszystkich eksperymemntów i wyciągnąć wniosek
#czy i jak proporcja podziału danych ma wpływ na jakośc klasyfikacji. Odpowiedni wniosek zapisać słownie
#w komentarzu na końcu komórki z rozwiązaniem.

import numpy as np
import pandas as pd
from sklearn import metrics, datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

dataset = pd.read_csv('../dane/rezygnacje.csv')
kolumny = ['CZAS_POSIADANIA','PLAN_MIEDZY', 'POCZTA_G','DZIEN_OPLATA','L_POL_BIURO','REZYGN']
dataset = dataset[kolumny]

noColumn = dataset.shape[1]
features = dataset.iloc[:,:noColumn-1] #Wyodrębnienie częśći warunkowej danych
labels = dataset.iloc[:,[noColumn-1]] #Wyodrębnienie kolumny decyzyjnej

#Parametr random_state to ziarno generatora liczb pseudolosowych (jesli parametr nie występuje, ziarno jest losowe])
#Ustalone ziarno pozwala na uzyskanie powtarzalnych wyników eksperymentów

test_sizes = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
accuracies = []

#Parametry tworzenia klasyfikatora
myNoNeighbors = 5 #Liczba sąsiadów
myMetric = 'euclidean' #Rodzaje odległości: 'euclidean', 'manhattan', 'minkowski'

for size in test_sizes:
    datasets = train_test_split(features, labels, test_size=size, random_state=1234)

    features_train = datasets[0]
    features_test = datasets[1]
    labels_train = datasets[2]
    labels_test = datasets[3]

    #Utworzenie obiektu przykładowego modelu klasyfikatora (k-NN)
    model = KNeighborsClassifier(n_neighbors=myNoNeighbors,metric=myMetric)
    model.fit(features_train, np.ravel(labels_train)) #Uczenie klasyfikatora na części treningowej

    labels_predicted = model.predict(features_test) #Generowania decyzji dla części testowej

    #Policzenie jakości klasyfikacji przez porównanie: labels_predicted i labels_test
    accuracy = metrics.accuracy_score(labels_test, labels_predicted)
    accuracies.append(accuracy)

    print("Dokładnośc klasyfikacji dla zbioru testowego ",size," całego zbioru =" ,accuracy)

    print("========= PEŁNE WYNIKI KLASYFIKACJI ================")

    report = classification_report(labels_test, labels_predicted)
    print(report )

    print("====== MACIERZ POMYŁEK (confusion matrix) =========")

    conf_matrix = confusion_matrix(labels_test, labels_predicted)
    print(conf_matrix)

#Objaśnienia do miar oceny klasyfikatora wypisywanych niżej:
# accuracy - dokładność klasyfikacji (liczba obiektów dobrze sklasyfikowanych / liczba wszystkich obiektów)
# precision - liczba obiektów dobrze sklasyf. z danej klasy / liczba wszystkich obiektów sklasyf. do danej klasy
# recall - liczba obiektów dobrze sklasyfikowanych z danej klasy / liczba wszystkich obiektów z danej klasy
# f1-score - średnia ważona precision i recall obliczana według wzoru: f1' - 2 * (precision * recall) / (precision + recall)
# support - liczba obiektów należących do danej klasy decyzyjnej

# Wykres porównujący dokładności klasyfikacji
plt.figure(figsize=(10, 6))
plt.plot([int(size*100) for size in test_sizes], accuracies, marker='o')
plt.title('Dokładność klasyfikacji w zależności od wielkości tablicy testowej')
plt.xlabel('Wielkość tablicy testowej (%)')
plt.ylabel('Dokładność klasyfikacji')
plt.grid(True)
plt.show()

#Wnioski: Podział na zbiór testowy i treningowy ma wpływ na dokładność klasyfikacji.
#Mniejszy zbiór testowy, a większy treningowy zwykle daje większą dokładność.
#Jednak podział po 50% również daje dość dużą dokładność. 