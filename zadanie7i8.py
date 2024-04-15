# --- Zadanie 7 i 8 ---

#W pliku tekstowym imiona.txt jest lista imion wraz z krotnością ich występowania w danej zbiorowości.
#Napisać program, który wczytuje dane z pliku i wylicza ile razy w sumie wystąpiło każde imię i wypisuje te
#informacje w kolejności od naczęściej wystepujących do najrzadziej. Krotności występowania dla danego imienia
#w różnych wierszach mają być oczywiście sumowane.
#Zadanie rozwiązać w dwóch wersjach:
#1. z wykorzystaniem listy,
#2. z wykorzystaniem słownika.

#ad 1. - z wykorzystaniem listy
lista_imion = []
krotnosc = []

#ad 2. - z wykorzystaniem słownika
slownik = {}

try:
    with open('imiona.txt', 'r', encoding='utf-8') as file:
        print(file)
        for line in file:
            text = line.strip()
            tokens = text.split(" ")
            if len(tokens) >= 2:
                name = tokens[0]
                lista_imion.append(name) #lista_imion
                quantity = int(tokens[1])
                krotnosc.append(quantity) #krotność
                slownik[name] = slownik.get(name, 0) + quantity #słownik
                #print("Odczytane:", name, quantity)
            else:
                print("Niepoprawny format linii:", line)
    file.close()
except Exception as excep:
    print("Błąd odczytu pliku: "+str(file))
    print("Powód błędu: "+str(excep))

#dla listy
lista_imion2 = []
lista_krotnosci = []

print("------ Lista: --------")
for imie in lista_imion:
    istnieje = False
    for j in range(len(lista_imion2)):
        if lista_imion2[j] == imie:
            lista_krotnosci[j] += krotnosc[lista_imion.index(imie)]
            istnieje = True
            break
    if not istnieje:
        lista_imion2.append(imie)
        lista_krotnosci.append(krotnosc[lista_imion.index(imie)])

# print(lista_imion2)
# print(lista_krotnosci)

# Połącz listę imion z listą krotności
lista_po_polaczeniu = list(zip(lista_imion2, lista_krotnosci))

# Posortuj listę po krotnościach w kolejności malejącej
lista_po_posortowaniu = sorted(lista_po_polaczeniu, key=lambda x: x[1], reverse=True)

# Wyświetl posortowaną listę
print("Posortowana lista:")
for element in lista_po_posortowaniu:
    print(element[0], ":", element[1])


#dla słownika
print("------ Słownik: --------")
slownik_wystapien = {}
for imie, ilosc in slownik.items():
    slownik_wystapien[imie] = slownik_wystapien.get(imie, 0) + ilosc

slownik_posortowany = dict(sorted(slownik_wystapien.items(), key=lambda item: item[1], reverse=True))
for imie, ilosc in slownik_posortowany.items():
    print(f"{imie} : {ilosc}")