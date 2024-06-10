#--- zdadanie 2 ---

# Zad 2. Wykorzystując pierwszą i drugą metodę dostępu do bazy danych opisane wyżej, napisz program który dokonuje
# podstawowej analizy statystycznej tabel REZYGNACJE i DREZYGNACJE w bazie JUPTEST
# (liczba wierszy, liczba kolumn, nazwy kolumn, typy wartości w kolumnach, liczba wartości w kolumnach,
# liczba pustych miejsc w tablicy).
# Dla analizy tabeli REZYGNACJE użyć pierwszą metodę dostępu do bazy danych opisaną wyżej. Natomiast dla analizy
# tabeli DREZYGNACJE użyć drugą metodę dostępu do bazy danych.
# Porównaj uzyskane wyniki dla obydwu tabel zestawiając je ze sobą. Czy bardzo różnią się między sobą?
# Wyniki i odpowiednie wnioski zapisać w komentarzu na końcu komórki z rozwiązaniem.

import pandas as pd
import sqlalchemy as db

# Dane dialektu i sterownika bazy danych
dialect = "postgresql"
driver = "psycopg2"

# Nazwa bazy danych
mydatabase = "mydatabase"

# Nazwa tabeli
# mytable =  "serce"
# mytable =  "dserce"
# mytable =  "rezygnacje"
# mytable =  "drezygnacje"

# Dane jak przy definiowaniu kontenera dockera
username = "admin"
password = "1234"
host = "mypostgres"
port = "5432"

# 1 metoda - pobieranie wszystkich danych na raz
mytable = "rezygnacje"
engine = db.create_engine(
    dialect + "+" + driver + "://" + username + ":" + password + "@" + host + ":" + port + "/" + mydatabase)
query = "select * from " + mytable
dataset_rezygnacje = pd.read_sql(sql=query, con=engine)

# analiza dla serca
rezygnacje_info = {
    'table': 'rezygnacje',
    'number_of_rows': dataset_rezygnacje.shape[0],
    'number_of_columns': dataset_rezygnacje.shape[1],
    # 'columns': dataset_rezygnacje.columns.tolist(),
    # 'data_types': dataset_rezygnacje.dtypes.to_dict(),
    'non_empty_counts': dataset_rezygnacje.count().to_dict(),
    'empty_counts': dataset_rezygnacje.isnull().sum().to_dict()
}

# 2 metoda
mytable = "drezygnacje"
part_size = 50000
i = 1
engine = db.create_engine(
    dialect + "+" + driver + "://" + username + ":" + password + "@" + host + ":" + port + "/" + mydatabase)
query = "select * from " + mytable

dataset_drezygnacje = pd.DataFrame()
for part in pd.read_sql_query(query, engine, chunksize=part_size):
    print("Dostęp do części tablicy numer:", i)
    # print(part) #Wypisanie aktualnej częśći
    i = i + 1
    dataset_drezygnacje = pd.concat([dataset_drezygnacje, part], ignore_index=True)

drezygnacje_info = {
    'table': 'DSERCE',
    'number_of_rows': dataset_drezygnacje.shape[0],
    'number_of_columns': dataset_drezygnacje.shape[1],
    # 'columns': dataset_drezygnacje.columns.tolist(),
    # 'data_types': dataset_drezygnacje.dtypes.to_dict(),
    'non_empty_counts': dataset_drezygnacje.count().to_dict(),
    'empty_counts': dataset_drezygnacje.isnull().sum().to_dict()
}

# print(f"Analiza dla serce info {serce_info}")
# print(f"Analiza dla dserce info {dserce_info}")

print("\nPorównanie wyników analizy tabel 'rezygnacje' i 'drezygnacje':")
comparison = {
    'number_of_rows': (rezygnacje_info['number_of_rows'], drezygnacje_info['number_of_rows']),
    'number_of_columns': (rezygnacje_info['number_of_columns'], drezygnacje_info['number_of_columns']),
    # 'columns': (rezygnacje_info['columns'], drezygnacje_info['columns']),
    # 'data_types': (rezygnacje_info['data_types'], drezygnacje_info['data_types']),
    'non_empty_counts': (rezygnacje_info['non_empty_counts'], drezygnacje_info['non_empty_counts']),
    'empty_counts': (rezygnacje_info['empty_counts'], drezygnacje_info['empty_counts'])
}

for key, (serce_val, dserce_val) in comparison.items():
    print(f"{key}: rezygnacje = {serce_val}, \n drezygnacje = {dserce_val}")
