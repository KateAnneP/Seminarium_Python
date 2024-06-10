#--- zadanie6 ---

#Wyznaczyć jakość dwóch klasyfikatorów wyznaczonych w poprzednim kroku poprzez wyliczenie ich kosztów
#marketingowych  błędnie podjętych decyzji przez program dla tablicy dz1_test.csv.
#Jeśli mamy dwie wartości decyzji: 1 (decyzja pozytywna - dobry kredyt) i 0 (decyzja negatywna - zły kredyt),
#to przy klasyfikacji obiektu testowego możliwe są 4 następujące przypadki:
#
#1. Prawdziwa klasyfikacja negatywna – nie przyznajemy kredytu i jest to decyzja poprawna, bo klient i tak by go
# nie spłacił (koszt=0).
#
#2. Prawdziwa klasyfikacja pozytywna – przyznajemy kredyt i jest to decyzja poprawna bo klient go spłaci (koszt=0).
#
#3. Fałszywa klasyfikacja negatywna – nie przyznajemy kredytu (klasyfikator wygenerował 0), ale nie jest to decyzja
# poprawna, bo klient spłaciłby kredyt (koszt=1).
#
#4. Fałszywa klasyfikacja pozytywna – przyznajemy kredyt (klasyfikator wygenerował 1), ale nie jest to decyzja poprawna,
# bo ten klient nie spłaci kredytu (koszt=5)
#
#Zauważmy, że koszt fałszywej klasyfikacji pozytywnej jest wyższy od kosztu fałszywej klasyfikacji negatywnej,
#gdyż w przypadku fałszywej klasyfikacji pozytywnej bank więcej straci ponosząc koszty zajmowania się nie spłaconym
#kredytem (np. koszty wynajęcia firmy w celu przeprowadzenia egzekucji komorniczej). Sumaryczny koszt marketingowy
#dla całej próbki testowej jest po prostu sumą kosztów marketingowych poniesionych dla wszystkich obiektów testowych.
#Dany klasyfikator jest lepszy, gdy ma mniejszy sumaryczny koszt marketingowy.  Podaj sumaryczne koszty marketingowe
#dla dwóch wymienionych wyżej klasyfikatorów.
#
#Wyniki i odpowiednie wnioski zapisać w komentarzu na końcu komórki z rozwiązaniem.


import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix

# Wczytanie danych z plików CSV, z uwzględnieniem separatora średnikowego
train_data = pd.read_csv('../dane/dz1_train.csv', sep=';')
test_data = pd.read_csv('../dane/dz1_test.csv', sep=';')

# Przygotowanie danych - podział na cechy (X) i etykiety (y)
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

# Koszty marketingowe
def calculate_costs(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    cost = fp * 5 + fn * 1
    return cost

cost_knn = calculate_costs(y_test, y_pred_knn)
cost_dt = calculate_costs(y_test, y_pred_dt)

# Wypisanie wyników
print("Klasyfikator k-NN:")
print("Dokładność: ", accuracy_knn)
print("Recall (klasa 0): ", recall_knn_class_0)
print("Recall (klasa 1): ", recall_knn_class_1)
print("Koszt marketingowy: ", cost_knn)

print("\nKlasyfikator Drzewo Decyzyjne:")
print("Dokładność: ", accuracy_dt)
print("Recall (klasa 0): ", recall_dt_class_0)
print("Recall (klasa 1): ", recall_dt_class_1)
print("Koszt marketingowy: ", cost_dt)

# Wnioski
# Wyniki klasyfikatorów pod względem dokładności, recall oraz kosztów marketingowych pokazują,
# który klasyfikator jest lepszy w kontekście różnych kryteriów oceny. Klasyfikator o niższym
# sumarycznym koszcie marketingowym będzie bardziej efektywny dla banku w kontekście minimalizacji
# strat finansowych związanych z błędnymi decyzjami kredytowymi.
