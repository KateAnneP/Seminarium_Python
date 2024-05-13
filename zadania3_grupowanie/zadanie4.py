# --- zadanie4 ---

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
#Do grupowania należy użyć tylko te dwa parametry. Grupowanie ma być wykonane metodą gęstościową DBSCAN.
#
#Wykonaj następujące polecenia.

#1. Wygenerować nową tablicę z 3 atrybutami: SUMA_MINUT (sumaryczna liczba minut), SUMA_KWOT (sumaryczna kwota
#zapłacona za rozmowy) oraz REZYGN i zapisać ją na dysku

#2.Wykonać optymalne grupowanie w taki sposób, aby liczba grup była podobna jak w Zadaniu 2 i 3.

#3. Scharakteryzować wszystkie skupienia z punktu widzenia wartości atrybutu REZYGN (chodzi o podanie informacji
#ile w każdym skupieniu jest klientów, którzy zrezygowali z usługi i takich, którzy nie zrezygmowali z usługi;
#przedstawić tę charakterystykę na wykresie słupkowym.

#4. Wykonaj wizualizację w dwóch wymiarach wyniku grupowania pokazując kolory wierszy należacych do skupień

#5. Porównać otrzymane skupienia ze skupieniami uzyskanymi w Zadaniu 2 i 3 (czy coś je łączy).

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering, DBSCAN
from sklearn.preprocessing import StandardScaler
import seaborn as sns

dane = pd.read_csv('../dane/rezygnacje.csv')

dane['SUMA_MINUT'] = dane['DZIEN_MIN'] + dane['WIECZOR_MIN'] + dane['NOC_MIN'] + dane['MIEDZY_MIN']
dane['SUMA_KWOT'] = dane['DZIEN_OPLATA'] + dane['WIECZ_OPLATA'] + dane['NOC_OPLATA'] + dane['MIEDZY_OPLATA']

nowa_tabela = dane[['SUMA_MINUT', 'SUMA_KWOT', 'REZYGN']]
#nowa_tabela.to_csv('nowa_tabela.csv', index=False)

scaler = StandardScaler()
tabela_scaled = scaler.fit_transform(nowa_tabela)

eps_range = [0.2, 0.5, 1, 1.5, 2, 2.5]
min_samples_range = [5, 10, 15, 20]

best_eps = None
best_min_samples = None
best_cluster_count = 0

for eps in eps_range:
    for min_samples in min_samples_range:
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        clusters = dbscan.fit_predict(tabela_scaled)
        cluster_count = len(set(clusters)) - (1 if -1 in clusters else 0)  # Ignorowanie outlierów
        if cluster_count > best_cluster_count:
            best_cluster_count = cluster_count
            best_eps = eps
            best_min_samples = min_samples

print(f"Optymalne parametry: eps={best_eps}, min_samples={best_min_samples}")

# Wykonanie grupowania DBSCAN z optymalnymi parametrami
dbscan = DBSCAN(eps=best_eps, min_samples=best_min_samples)
clusters = dbscan.fit_predict(tabela_scaled)

# Liczenie liczby skupień
num_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
print(f"Liczba skupień: {num_clusters}")

nowa_tabela['Cluster'] = clusters

# Charakterystyka skupień z punktu widzenia wartości atrybutu REZYGN
cluster_characteristics = nowa_tabela.groupby(['Cluster', 'REZYGN']).size().unstack(fill_value=0)
print("Charakterystyka skupień z punktu widzenia wartości atrybutu REZYGN:")
print(cluster_characteristics)

# Wykres słupkowy przedstawiający charakterystykę skupień z punktu widzenia wartości atrybutu REZYGN
plt.figure(figsize=(10, 6))
sns.countplot(data=nowa_tabela, x='Cluster', hue='REZYGN')
plt.title("Charakterystyka skupień z punktu widzenia wartości atrybutu REZYGN")
plt.xlabel("Numer klastra")
plt.ylabel("Liczba klientów")
plt.legend(title='REZYGN', loc='upper right')
plt.show()

# Wizualizacja wyniku grupowania w dwóch wymiarach
plt.figure(figsize=(10, 6))
sns.scatterplot(data=nowa_tabela, x='SUMA_MINUT', y='SUMA_KWOT', hue='Cluster', palette='tab10', legend='full')
plt.title("Wizualizacja wyniku grupowania w dwóch wymiarach")
plt.xlabel("Suma minut rozmowy")
plt.ylabel("Suma kwoty zapłaconej za rozmowy")
plt.legend(title='Cluster', loc='upper right')
plt.show()



