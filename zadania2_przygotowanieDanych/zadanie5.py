# --- zadanie5 ---

#Wyznacz ranking skorelowania w danych rezygnacje.csv wszystkich par kolumn.
#Dane dotyczą możliwości rezygnacji z usługi sieci telefonii komórkowej przez jej klientów.
#Każdy wiersz opisuje sytuację klienta, a ostatnia kolumna reprezentuje informację czy klient niedługo zrezygniuje
#czy nie zrezygnuje.
#Oceń czy policzone korelacje jakoś wiążą się z wiedzą dziedzinową na ten temat, tzn. która wartość korelacji wydaje
#się uzasadniona, a która nieuzasadniona.

#Oto opis kolumn:

#STAN – kod stanu USA (nominalna),
#CZAS_POSIADANIA -  czas posiadania usługi (numeryczna)
#KOD_OBSZARU – kod obszaru kraju (nominalna),
#NR_TEL – numer telefonu (pełni rolę ID - nominalna),
#PLAN_MIEDZY – czy klient przystąpił do planu międzynarodowego (nominalna),
#POCZTA_G – czy klient przystąpił do planu poczty głosowej (nominalna),
#L_WIAD_POCZTA_G – liczba wiad.w poczcie głosowej (numeryczna),
#DZIEN_MIN – liczba minut rozmów w dzień (numeryczna),
#DZIEN_L_POL – liczba połączeń w dzień (numeryczna),
#DZIEN_OPLATA – opłata za rozmowy w dzień (numeryczna),
#WIECZOR_MIN – liczba minut rozmów wieczorami (numeryczna),
#WIECZ_L_POL – liczba połączeń wieczorami (numeryczna),
#WIECZ_OPLATA – opłata za rozmowy wieczorem (numeryczna),
#NOC_MIN – liczba minut rozmów nocnych (numeryczna),
#NOC_L_POL – liczba połączeń nocnych (numeryczna),
#NOC_OPLATA – opłata za rozmowy w nocy (numeryczna),
#MIEDZY_MIN – liczba minut na połączenia międzynarodowe (numeryczna),
#MIEDZY_L_POL – liczba połączeń międzynarodowych (numeryczna),
#MIEDZY_OPLATA – opłata za rozmowy międzynarodowe (numeryczna),
#L_POL_BIURO – liczba połączeń z biurem obsługi klienta (numeryczna),
#REZYGN – informacja o rezygnacji z usługi (nominalna).

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dane = pd.read_csv('../dane/rezygnacje.csv')

correlation_matrix = dane.corr(numeric_only=True)

# Wizualizacja macierzy korelacji za pomocą heatmapy
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Macierz korelacji dla danych rezygnacje.csv")
plt.show()

# Ranking skorelowania dla kolumny 'REZYGN'
correlation_with_resignation = correlation_matrix['REZYGN'].sort_values(ascending=False)
print("Ranking skorelowania dla kolumny 'REZYGN':")
print(correlation_with_resignation)