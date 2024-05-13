# --- zadanie2 ---

#Firma świadcząca usługi telekomunikacyjne chce wykonać eksplorację swoich danych celem odkrycia wiedzy
#użytecznej do przewidywania możliwości rezygnacji klientów z pewnej usługi. Dane firmy znajdują się
#w pliku rezygnacje.csv.
#Do eksploracji wytypowano grupowanie obiektów. Tym razem analizy mają dotyczyć dwóch parametrów klienta:
#sumaryczna liczba minut rozmowy oraz sumaryczna kwota zapłacona za rozmowy.
#
#Sumaryczna liczba minut rozmowy dla danego klienta, to suma wartości z kolumn:
# DZIEN_MIN, WIECZOR_MIN, NOC_MIN, MIEDZY_MIN,
#
#Sumaryczna kwota zapłacona za rozmowy dla danego klienta, to suma wartości z kolumn:
# DZIEN_OPLATA,WIECZ_OPLATA,NOC_OPLATA,MIEDZY_OPLATA
#
#Do grupowania należy użyć tylko te dwa parametry. Grupowanie ma być wykonane metodą k-średnich (k-means)
#z odległością euklidesową, ale nie jest od początku znana liczba środków.
#
#Wykonaj następujące polecenia.

#1. wygenerować nową tablicę z 3 atrybutami: SUMA_MINUT (sumaryczna liczba minut), SUMA_KWOT (sumaryczna kwota
#zapłacona za rozmowy) oraz REZYGN i zapisać ją na dysku

#2. Metodą łokcia wyznaczyć optymalną liczbę skupień dla atrybutów SUMA_MINUT i SUMA_KWOT oraz wykonać
#optymalne grupowanie.

#3. Scharakteryzować wszystkie skupienia z punktu widzenia wartości atrybutu REZYGN (chodzi o podanie informacji
#ile w każdym skupieniu jest klientów, którzy zrezygowali z usługi i takich, którzy nie zrezygmowali z usługi;
#przedstawić tę charakterystykę na wykresie słupkowym.

#4 Wykonaj wizualizację w dwóch wymiarach wyniku grupowania pokazując środki skupień na tle punktów reprezentujących
#wiersze z danych.

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

dane = pd.read_csv('../dane/rezygnacje.csv')

dane['SUMA_MINUT'] = dane['DZIEN_MIN'] + dane['WIECZOR_MIN'] + dane['NOC_MIN'] + dane['MIEDZY_MIN']
dane['SUMA_KWOT'] = dane['DZIEN_OPLATA'] + dane['WIECZ_OPLATA'] + dane['NOC_OPLATA'] + dane['MIEDZY_OPLATA']

dane_grupowanie = dane[['SUMA_MINUT', 'SUMA_KWOT', 'REZYGN']]
dane_grupowanie.to_csv('rezygnacje_grupowanie.csv', index=False)

scaler = StandardScaler ()
dane_standaryzowane = scaler.fit_transform(dane_grupowanie[['SUMA_MINUT', 'SUMA_KWOT']])

results = []
for k in range(1, 10):
    # Utworzenie obiektu do grupowania
    kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300, random_state=0)
    kmeans.fit(dane_standaryzowane)

    # Obliczenie jakości grupowania
    # Miara niespójności skupień: suma kwadratów odległości obiektów do środka najbliższego skupienia
    inertia = kmeans.inertia_  # Powinna być jak najmniejsza

    results.append(inertia)

    print("*** Eksperyment numer:" + str(k) + " Jakość=", inertia)

# Na podstawie poniższego wykresu wybieramy takie k, które jest bliskie punktu przegięcia

fig = plt.figure(figsize=(10, 7))
plt.plot(range(1, 10), results, marker='o')
plt.xlabel('Liczba skupień')
plt.ylabel('Miara niespójności')
plt.tight_layout()
plt.show()

# Wykonanie optymalnego grupowania
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
dane_grupy = kmeans.fit_predict(dane_standaryzowane)

# Dodanie informacji o skupieniach do danych
dane_grupowanie['SKUPIENIE'] = dane_grupy

# Scharakteryzowanie skupień z punktu widzenia wartości atrybutu REZYGN
charakterystyka = dane_grupowanie.groupby(['SKUPIENIE', 'REZYGN']).size().unstack(fill_value=0)

charakterystyka.plot(kind='bar', stacked=True)
plt.title('Charakterystyka skupień z punktu widzenia wartości atrybutu REZYGN')
plt.xlabel('Skupienie')
plt.ylabel('Liczba klientów')
plt.xticks(rotation=0)
plt.legend(title='Rezygnacja', labels=['Nie', 'Tak'])
plt.show()




