# --- zadanie1 ---

#Firma świadcząca usługi telekomunikacyjne chce wykonać eksplorację swoich danych celem odkrycia wiedzy
#użytecznej do przewidywania możliwości rezygnacji klientów z pewnej usługi. Dane firmy znajdują się
#w pliku rezygnacje.csv.
#Do eksploracji wytypowano grupowanie obiektów. Ponadto, na podstawie wcześniejszych analiz ustalono,
#że do grupowania należy użyć tylko następujące atrybuty: PLAN_MIEDZY i POCZTA_G.
#Ponadto, grupowanie ma być wykonane metodą k-średnich (k-means) z liczbą środków 3 i odległością euklidesową.
#Wykonaj grupowanie obiektów, a następnie poniższe polecenia.
#
#1. podać liczebności wszystkich 3 skupień,
#2. scharakteryzować wszystkie skupienia z punktu widzenia wartości atrybutu REZYGN (chodzi o podanie informacji
#ile w każdym skupieniu jest klientów, którzy zrezygowali z usługi i takich, którzy nie zrezygmowali z usługi);
#przedstawić tę charakterystykę na wykresie słupkowym,
#3. dla 5 ostatnich obiektów w danych podać do jakiego skupienia należą,
#4. za pomocą skonstruowanego wyżej modelu grupowania sklasyfikować do odpowiedniego skupienia klienta, który
#ma wyłączoną pocztę głosową (POCZTA_G=0), ale ma włączony plan międzynarodowy (PLAN_MIEDZY=1).

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

dane = pd.read_csv('../dane/rezygnacje.csv')
dane_grupowanie = dane[['PLAN_MIEDZY', 'POCZTA_G']]

kmeans = KMeans(n_clusters=3, random_state=42) #Grupowanie
kmeans.fit(dane_grupowanie)
dane['SKUP'] = kmeans.labels_

liczebnosci = dane['SKUP'].value_counts().sort_index()
print("Liczebności skupień:")
print(liczebnosci)

charakterystyka = dane.groupby(['SKUP', 'REZYGN']).size().unstack(fill_value=0)
print("\nCharakterystyka skupień z punktu widzenia wartości atrybutu REZYGN:")
print(charakterystyka)

charakterystyka.plot(kind='bar', stacked=True)
plt.title('Charakterystyka skupień z punktu widzenia wartości atrybutu REZYGN')
plt.xlabel('Skupienie')
plt.ylabel('Liczba klientów')
plt.xticks(rotation=0)
plt.legend(title='REZYGN', loc='upper right')
plt.show()

print("Dla 5 ostatnich obiektów w danych:")
print(dane.tail())

# Klasyfikacja klienta z wyłączoną pocztą głosową i włączonym planem międzynarodowym
nowy_klient = pd.DataFrame({'PLAN_MIEDZY': [1], 'POCZTA_G': [0]})
skup_nowego_klienta = kmeans.predict(nowy_klient)
print("\nSkupienie nowego klienta:", skup_nowego_klienta)