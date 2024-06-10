#--- zadanie4 ---

#Napisz program który odczytuje tablicę danych rezygnacje.csv oraz wybiera z niej wszystkie wiersze oraz
#kolumny: CZAS_POSIADANIA, PLAN_MIEDZY, POCZTA_G, L_WIAD_POCZTA_G, L_POL_BIURO, REZYGN.
#Następnie wykonuje szereg eksperymentów tak jak w poprzednim przykładzie celem ustalenia który klasyfikator
#uzyskuje najlepsze wyniki. Poeksperymentować trochę z parametrami tych 4 klasyfikatorów, aby uzyskać lepszą jakość
#klasyfikacji. Wykonać wykres porównujący jakości klasyfikacji (accuracy) dla wszystkich 4 klasyfikatorów
#i wyciągnąć wniosek który klasyfikator jest najlepszy.
#Wygenerować krzywe ROC dla wszystkich 4 klasyfikatorów.
#Czy rankingi klasyfikatorów z punktu wudzenia accuracy oraz AUC pokrywają się?
#Odpowiedni wniosek zapisać słownie w komentarzu na końcu komórki z rozwiązaniem.
#Sprawdzić czy dodanie innych atrybutów warunkowych, które zostały wcześniej usunięte, poprawi jakość klasyfikatorów.
#Odpowiedni wniosek na ten temat także zapisać słownie w komentarzu na końcu komórki z rozwiązaniem.

import numpy as np
import pandas as pd
from sklearn import metrics, datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
import matplotlib.pyplot as plt

dataset = pd.read_csv('../dane/rezygnacje.csv')
kolumny = ['CZAS_POSIADANIA','PLAN_MIEDZY', 'POCZTA_G', 'L_WIAD_POCZTA_G','L_POL_BIURO','REZYGN']
dataset = dataset[kolumny]

noColumn = dataset.shape[1]
features = dataset.iloc[:,:noColumn-1]
labels = dataset.iloc[:,[noColumn-1]]

#Podział tablicy na część treningową i testową
data = train_test_split(features, labels, test_size=0.6, random_state=12345)
features_train = data[0]
features_test = data[1]
labels_train = data[2]
labels_test = data[3]

#========DEFINIOWANIE MODELI i ich nazw ===============

models = []
modelNameList = []

#Klasyfikator k najbliższych sąsiadów
model = KNeighborsClassifier(n_neighbors=3,metric = 'euclidean')
models.append(model)
modelNameList.append("KNN")

#Naiwny Bayes traktujący atrybuty jako atrybuty z ciągłymi wartościami (dobry dla numerycznych)
model = GaussianNB()
models.append(model)
modelNameList.append("GaussianNB")

#Naiwny Bayes traktujący atrybuty jako atrybuty z dyskretnymi wartościami (dobry dla symbolicznych)
model = BernoulliNB()
models.append(model)
modelNameList.append("BernoulliNB")

#Drzewo decyzyjne
model = tree.DecisionTreeClassifier(max_depth=5)
models.append(model)
modelNameList.append("DecisionTree")


#===========================================

results = []
accuracies = []

#Testowanie wszystkich klasyfikatorów
for i in range(0,len(models)):
    model = models[i]
    model.fit(features_train, np.ravel(labels_train))
    labels_predicted = model.predict(features_test) # Policzenie pola pod krzywą ROC

    auc = metrics.roc_auc_score(labels_test, labels_predicted)

    # Policzenie prawdopodobieństw
    target_probabilities = model.predict_proba(features_test)[:, 1]

    # Wyznaczenie danych do krzywej ROC
    czulosci, specyficznosci, progi = metrics.roc_curve(labels_test, target_probabilities, pos_label=1)

    print("Użyte progi prawdopodobieństwa:", progi)
    print("AUC=", auc)

    plt.figure(figsize=(10, 8))  # Rozmiary okna z wykresem
    plt.plot(czulosci, specyficznosci)
    plt.title("Krzywa ROC")
    plt.xlabel("1-Specyficzność")
    plt.ylabel("Czułość")
    plt.show()

    accuracy = metrics.accuracy_score(labels_test, labels_predicted)
    locList = []; locList.append(accuracy); locList.append(modelNameList[i])
    results.append(locList)
    accuracies.append(accuracy)

def myFunc(result):
    return result[0]  #Funkcja porównuje według accuracy

#Sortowanie wyników
results.sort(reverse=True, key=myFunc)

#Wypisanie posortowanych wyników
for i in range(0,len(results)):
    result = results[i]
    print(str(i+1)+".",result[0],result[1])

# Wykres porównujący dokładności klasyfikacji
#plt.figure(figsize=(10, 6))
plt.plot(modelNameList, accuracies, marker='o')
plt.title('Porównanie dokładności klasyfikacji')
plt.xlabel('Metoda')
plt.ylabel('Dokładność klasyfikacji')
plt.grid(True)
plt.show()

#Wniosek: Najlepszy jest klasyfikator drzewa decyzyjnego