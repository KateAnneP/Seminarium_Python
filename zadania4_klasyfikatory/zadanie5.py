#--- zadanie5 ---

#Pewien bank zgromadził dane o kredytach, które oferował swoim klientom oraz informacje czy każdy z tych
#kredytów był dobrym kredytem dla banku (klient spłacił kredyt) lub złym kredytem dla banku (klient nie spłacił
#kredytu).  Dane te mają posłużyć do automatycznego  wspomagania podejmowania decyzji w zakresie przyznawania
#kredytów nowym klientom za pomocą klasyfikatorów. W celu przeprowadzenia testu efektywności wybranych
#klasyfikatorów metodą train&test dane podzielono na dwie części, które są dostępne w plikach w formacie CSV:
# dz1_train.csv i dz1_test.csv.
#
#Przeprowadzić test tablicy dz1_test.csv metodą train&test dla następujących klasyfikatorów:
#
#1. klasyfikator oparty na metodzie k-NN biorący pod uwage 5 najbliższych sąsiadów i metrykę euklidesową,
#
#2. klasyfikator oparty na drzewie decyzyjnym skonstruowanym według miary entropijnej podziału węzła,
# maksymalną głebokością drzewa równą 6 i minimalnym wymaganym spadkiem niejednorodności równym 0.01
# (pozostałe parametry na ustawieniach standardowych).
#
#Wypisać dokładność klasyfikacji obydwu klasyfikatorów (accuracy) dla całej tablicy testowej oraz
#dla obydwu klas decyzyjnych z osobna (recall) (jest to 6 liczb).
#
#Wyniki i odpowiednie wnioski na temat porównania klasyfikatorów odnośnie ich jakości zapisać w komentarzu na
#końcu komórki z rozwiązaniem.

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score

# Wczytanie danych
train_data = pd.read_csv('../dane/dz1_train.csv', sep=';')
test_data = pd.read_csv('../dane/dz1_test.csv', sep=';')


# Przygotowanie danych
X_train = train_data.iloc[:, :-1]
y_train = train_data.iloc[:, -1]
X_test = test_data.iloc[:, :-1]
y_test = test_data.iloc[:, -1]

# Klasyfikator k-NN
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# Klasyfikator drzewo decyzyjne
dt = DecisionTreeClassifier(criterion='entropy', max_depth=6, min_impurity_decrease=0.01)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

# Ocena klasyfikatora k-NN
accuracy_knn = accuracy_score(y_test, y_pred_knn)
recall_knn_class_0 = recall_score(y_test, y_pred_knn, pos_label=0)
recall_knn_class_1 = recall_score(y_test, y_pred_knn, pos_label=1)

# Ocena klasyfikatora drzewa decyzyjnego
accuracy_dt = accuracy_score(y_test, y_pred_dt)
recall_dt_class_0 = recall_score(y_test, y_pred_dt, pos_label=0)
recall_dt_class_1 = recall_score(y_test, y_pred_dt, pos_label=1)

# Wypisanie wyników
print("Klasyfikator k-NN:")
print("Dokładność: ", accuracy_knn)
print("Recall (klasa 0): ", recall_knn_class_0)
print("Recall (klasa 1): ", recall_knn_class_1)

print("\nKlasyfikator Drzewo Decyzyjne:")
print("Dokładność: ", accuracy_dt)
print("Recall (klasa 0): ", recall_dt_class_0)
print("Recall (klasa 1): ", recall_dt_class_1)
