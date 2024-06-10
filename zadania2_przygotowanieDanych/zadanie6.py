# --- zadanie6 ---

#Napisz program który dokonuje analizy statystycznej kolumn zbioru danych rezygnacje.csv, przy czym kolumny
#o wartościach symbolicznych (nominalne) analizuje inaczej, a kolumny o wartościach numerycznych inaczej.
#Porównaj, czy uzyskane wyniki zgadzają się z tym co wypisze funkcja describe() dla całej tablicy.

import pandas as pd

rezygnacje = pd.read_csv('../dane/rezygnacje.csv')

# Podział kolumn na numeryczne i symboliczne
kolumny_numeryczne = rezygnacje.select_dtypes(include=['float64', 'int64']).columns
kolumny_symboliczne = rezygnacje.select_dtypes(include=['object']).columns

print("Analiza statystyczna kolumn numerycznych:")
print(rezygnacje[kolumny_numeryczne].describe())

print("Analiza statystyczna kolumn symbolicznych:")
for col in kolumny_symboliczne:
    print("Kolumna:", col)
    print(rezygnacje[col].value_counts())
    print("\n")

print("\nAnaliza dla całości danych: ")
print(rezygnacje.describe())

