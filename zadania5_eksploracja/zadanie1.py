#--- zadanie1 ---

#Wykorzystując pierwszą i drugą metodę dostępu do bazy danych opisane wyżej, napisz program który dokonuje
#podstawowej analizy statystycznej tabel SERCE i DSERCE w bazie JUPTEST
#(liczba wierszy, liczba kolumn, nazwy kolumn, typy wartości w kolumnach, liczba wartości w kolumnach,
#liczba pustych miejsc w tablicy).
#Dla analizy tabeli SERCE użyć pierwszą metodę dostępu do bazy danych opisaną wyżej. Natomiast dla analizy
#tabeli DSERCE użyć edrugą metodę dostępu do bazy danych.
#Porównaj uzyskane wyniki dla obydwu tabel zestawiając je ze sobą. Czy bardzo różnią się między sobą?
#Wyniki i odpowiednie wnioski zapisać w komentarzu na końcu komórki z rozwiązaniem.

import pandas as pd
import sqlalchemy as db

#Dane dialektu i sterownika bazy danych
dialect = "postgresql"
driver = "psycopg2"

#Nazwa bazy danych
mydatabase = "mydatabase"

#Nazwa tabeli
#mytable =  "serce"
#mytable =  "dserce"
#mytable =  "rezygnacje"
#mytable =  "drezygnacje"

#Dane jak przy definiowaniu kontenera dockera
username = "admin"
password = "1234"
host = "mypostgres"
port = "5432"

# 1 metoda - Pobieranie wszystkich danych na raz
mytable =  "serce"
engine = db.create_engine(dialect+"+"+driver+"://"+username+":"+password+"@"+host+":"+port+"/"+mydatabase)
query = "select * from "+mytable
dataset_serce = pd.read_sql(sql=query, con=engine)

# analiza dla serca
serce_info = {
    'table': 'SERCE',
    'number_of_rows': dataset_serce.shape[0],
    'number_of_columns': dataset_serce.shape[1],
    #'columns': dataset_serce.columns.tolist(),
    #'data_types': dataset_serce.dtypes.to_dict(),
    'non_empty_counts': dataset_serce.count().to_dict(),
    'empty_counts': dataset_serce.isnull().sum().to_dict()
}


# 2 metoda - Pobieranie danych porcjami
mytable =  "dserce"
part_size = 50000
i = 1
engine = db.create_engine(dialect+"+"+driver+"://"+username+":"+password+"@"+host+":"+port+"/"+mydatabase)
query = "select * from "+mytable

dataset_dserce = pd.DataFrame()
for part in pd.read_sql_query(query , engine, chunksize=part_size):
    print("Dostęp do części tablicy numer:",i)
    i = i + 1
    dataset_dserce = pd.concat([dataset_dserce, part], ignore_index=True)

dserce_info = {
    'table': 'DSERCE',
    'number_of_rows': dataset_dserce.shape[0],
    'number_of_columns': dataset_dserce.shape[1],
    #'columns': dataset_dserce.columns.tolist(),
    #'data_types': dataset_dserce.dtypes.to_dict(),
    'non_empty_counts': dataset_dserce.count().to_dict(),
    'empty_counts': dataset_dserce.isnull().sum().to_dict()
}

#print(f"Analiza dla serce info {serce_info}")
#print(f"Analiza dla dserce info {dserce_info}")

print("\nPorównanie wyników analizy tabel 'SERCE' i 'DSERCE':")
comparison = {
    'number_of_rows': (serce_info['number_of_rows'], dserce_info['number_of_rows']),
    'number_of_columns': (serce_info['number_of_columns'], dserce_info['number_of_columns']),
    #'columns': (serce_info['columns'], dserce_info['columns']),
    #'data_types': (serce_info['data_types'], dserce_info['data_types']),
    'non_empty_counts': (serce_info['non_empty_counts'], dserce_info['non_empty_counts']),
    'empty_counts': (serce_info['empty_counts'], dserce_info['empty_counts'])
}

for key, (serce_val, dserce_val) in comparison.items():
    print(f"{key}: SERCE = {serce_val}, \n DSERCE = {dserce_val}")


#Różnicą jest wielkość rekordów