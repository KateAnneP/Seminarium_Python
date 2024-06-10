#Program będący testerem klienta, czy zrezygnuje z usługi, czy nie.
#Jest menu, podaje się liczbę klienta, plan międzynarodowy i poczta głosowa, dzień_opłata (od 10 do 100), L_pol_biuro
#(ile razy zadzwonił do biura obsługi klienta, od 0 do pięciu)
#Pytanie: Podaj dane klienta, czas posiadania (liczba całkowita od 1 do 200 dni), plan (tak 1/nie 0), poczta(tak/nie)
#Naciskamy enter i wyświetla się przewidywana decyzja - czy zrezygnuje, czy nie. Bez GUI.
#Za pomocą przykładu z lasem losowym, trzeba się pozbyć atrybutów symolicznych
#Atrybuty liczbowe: 1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19; 20 to decyzja - ale tworzymy klasyfikator tylko na czterech
#Walidacja wprowadzanych danych
#Tworzymy klasyfikator na podstawie tych czterech cech i decyzji

import pandas as pd
import numpy as np
from sklearn import metrics, datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

print("---------------------------------")
print("Wybierz opcję: ")
print("1 - predykcja")
print("0 - wyjście z programu")
wybor = int(input("Twój wybór: "))
while(wybor == 1):
    print("Podaj dane klienta: ")
    plan_miedzynarodowy = input("Podaj, czy klient posiada plan międzynarodowy (0-nie/1-tak): ")
    poczta = input("Podaj, czy klient posiada pocztę głosową (0-nie/1-tak): ")
    dzien_oplata = input("Podaj opłatę za jeden dzień: ")
    L_pol_biuro = input("Podaj liczbę połączeń do biura obsługi klienta: ")

    dane = pd.read_csv('dane/rezygnacje.csv')
    #print(dane)

    kolumny = ['PLAN_MIEDZY', 'POCZTA_G','DZIEN_OPLATA','L_POL_BIURO','REZYGN']
    data = dane[kolumny]
    # print(data.head())
    # print(data.tail())

    noColumn = data.shape[1] #Ustalenie liczby kolumn w danych

    features = data.iloc[:,:noColumn-1] #Wyodrębnienie częśći warunkowej danych
    #print(features)
    labels = data.iloc[:,[noColumn-1]] #Wyodrębnienie kolumny decyzyjnej
    #print(labels)

    #Utworzenie obiektu przykładowego modelu lasu losowego
    model = RandomForestClassifier()
    model.fit(features, np.ravel(labels)) #Uczenie klasyfikatora

    row = []
    row.append(plan_miedzynarodowy)
    row.append(poczta)
    row.append(dzien_oplata)
    row.append(L_pol_biuro)

    kol = features.columns.values

    row_list = []
    row_list.append(row)

    dataset = pd.DataFrame(row_list, columns=kol)
    labels_predicted = model.predict(dataset)

    if (labels_predicted == 1):
        print(f"Predicted: klient zrezygnuje")
    else:
        print(f"Predicted: klient niezrezygnuje")

    wybor = int(input("Czy chcesz dalej wykonywać predykcję (1 - tak/0 - wyjście)? Twój wybór: "))