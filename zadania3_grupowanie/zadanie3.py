# --- zadanie3 ---

#Firma świadcząca usługi telekomunikacyjne chce wykonać eksplorację swoich danych celem odkrycia wiedzy
#użytecznej do przewidywania możliwości rezygnacji klientów z pewnej usługi. Dane firmy znajdują się
#w pliku rezygnacje.csv.
#Do eksploracji wytypowano grupowanie obiektów. Analizy mają dotyczyć dwóch parametrów klienta:
#sumaryczna liczba minut rozmowy oraz sumaryczna kwota zapłacona za rozmowy.
#
#Sumaryczna liczba minut rozmowy dla danego klienta, to suma wartości z kolumn:
# DZIEN_MIN, WIECZOR_MIN, NOC_MIN, MIEDZY_MIN,
#
#Sumaryczna kwota zapłacona za rozmowy dla danego klienta, to suma wartości z kolumn:
# DZIEN_OPLATA,WIECZ_OPLATA,NOC_OPLATA,MIEDZY_OPLATA
#
#Do grupowania należy użyć tylko te dwa parametry. Grupowanie ma być wykonane metodą hierarchiczną.
#
#Wykonaj następujące polecenia.

#1. Wygenerować nową tablicę z 3 atrybutami: SUMA_MINUT (sumaryczna liczba minut), SUMA_KWOT (sumaryczna kwota
#zapłacona za rozmowy) oraz REZYGN i zapisać ją na dysku

#2.Wykonać optymalne grupowanie w taki sposób, aby liczba grup była podobna jak w Zadaniu 2.

#3. Scharakteryzować wszystkie skupienia z punktu widzenia wartości atrybutu REZYGN (chodzi o podanie informacji
#ile w każdym skupieniu jest klientów, którzy zrezygowali z usługi i takich, którzy nie zrezygmowali z usługi;
#przedstawić tę charakterystykę na wykresie słupkowym.

#4. Wykonaj wizualizację w dwóch wymiarach wyniku grupowania pokazując kolory wierszy należacych do skupień

#5. Porównać otrzymane skupienia ze skupieniami uzyskanymi w Zadaniu 2 (czy coś je łączy).

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering

dane = pd.read_csv('../dane/rezygnacje.csv')

dane['SUMA_MINUT'] = dane['DZIEN_MIN'] + dane['WIECZOR_MIN'] + dane['NOC_MIN'] + dane['MIEDZY_MIN']
dane['SUMA_KWOT'] = dane['DZIEN_OPLATA'] + dane['WIECZ_OPLATA'] + dane['NOC_OPLATA'] + dane['MIEDZY_OPLATA']

ac = AgglomerativeClustering(n_clusters=4, metric='euclidean', linkage='complete')
ac.fit(dane)

clusters = ac.fit_predict(dane)

for i in range(0,len(clusters)):
    print("Obiekt numer:"+str(i+1)," Skupienie:"+str(clusters[i]))

dane['SKUPIENIE'] = dane

# Scharakteryzowanie skupień z punktu widzenia wartości atrybutu REZYGN
charakterystyka = dane.groupby(['SKUPIENIE', 'REZYGN']).size().unstack(fill_value=0)

charakterystyka.plot(kind='bar', stacked=True)
plt.title('Charakterystyka skupień z punktu widzenia wartości atrybutu REZYGN')
plt.xlabel('Skupienie')
plt.ylabel('Liczba klientów')
plt.xticks(rotation=0)
plt.legend(title='Rezygnacja', labels=['Nie', 'Tak'])
plt.show()