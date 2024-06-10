#Kierownik sklepu spożywczego zdecydował się dokonać sprawdzenia rozlokowania towarów na terenie sklepu w ten sposób,
#aby zwiększyć sprzedaż. W tym celu postanowił zlecić wykonanie eksploracji swoich danych. Ponieważ dane, którymi
#dysponuje dotyczą transakcji dokonywanych na kasach fiskalnych (zawartość paragonów), naturalną metodą eksploracji
#pasująca do tych danych jest generowanie reguł asocjacyjnych pomiędzy produktami w koszyku zakupów.
#W związku z tym zostałeś poproszony o przeprowadzenie eksploracji tą metodą oraz o wykonanie kilku poniższych poleceń.
#Reguły asocjacyjne mają być liczone metodą Apriori, przy czym mają być wyliczone wszystkie reguły o wsparciu co najmniej
#20 procent wierszy i ufności co najmniej 0.6.

#a) podać regułę (lub reguły) o ufności 1.0 i wsparciu co najmniej 0.3 oraz średnią ufność wszystkich wyliczonych
#reguł asocjacyjnych i ich średnie wsparcie.

#b) wykorzystując wyliczone reguły asocjacyjne, podać produkty, które powinny być blisko produktu „płatki” zakładając,
#że są to produkty, występujące w następnikach reguł o wsparciu nie mniejszym niż 0.7, ufności co najmniej 0.3 i mających
#w poprzedniku produkt „płatki”,

#c) wykorzystując wyliczone reguły asocjacyjne podać produkty, które silnie wspierają sprzedaż produktu jajka,
#tzn. jajka powinny być umieszczone blisko tych produktów (brać pod uwagę reguły ze wsparciem co najmniej 0.3 i ufności
#co najmniej 0.6 z produktem "jajka" w następniku).

from efficient_apriori import apriori
import pandas as pd

dataset = pd.read_csv('./dane/koszyki.csv',sep=',')

#print(dataset.head())

def getTupleList(dataset):
    noRow = dataset.shape[0]
    noColumn = dataset.shape[1]

    column_list = list(dataset.columns.values)  # Pobranie listy nazw kolumn

    output_tuple_list = []

    for i in range(0, noRow):  # Przegladanie wierszy
        basket = []
        for j in range(0, noColumn):  # Przegladanie kolumn
            value = dataset.iat[i, j]
            if value == "tak":
                basket.append(column_list[j])

        if len(basket) > 0:
            locTuple = tuple(basket)
            output_tuple_list.append(locTuple)

    return output_tuple_list

transactions = getTupleList(dataset)

#print(transactions)

#Obliczenie reguł asocjacyjnych
itemsets, rules = apriori(transactions, min_support=0.2, min_confidence=0.6)

#Wypisanie wszystkich reguł
# for i in range(0,len(rules)):
#     rule = rules[i]
#     left_side = list(rule.lhs)
#     right_side = list(rule.rhs)
#     confidence = rule.confidence
#     support = rule.support
#     print(i+1,left_side,"=>",right_side,confidence,round(support,3)) #Wypisanie reguły

suma_ufnosci = 0
suma_wsparcia = 0

#a) reguły o ufności 1.0 i wsparciu co najmniej 0.3
print("Reguły o ufności 1.0 i wsparciu co najmniej 0.3")

for i in range(0,len(rules)):
    rule = rules[i]
    left_side = list(rule.lhs)
    right_side = list(rule.rhs)
    confidence = rule.confidence
    suma_ufnosci += confidence
    support = rule.support
    suma_wsparcia += support
    if (confidence == 1.0 and support >= 0.3):
        print(i+1,left_side,"=>",right_side,confidence,round(support,3)) #Wypisanie reguły

srednia_ufnosc = suma_ufnosci/len(rules)
srednie_wsparcie = suma_wsparcia/len(rules)

#print(f"Średnie wsparcie wynosi: {srednie_wsparcie}, a średnia ufność: {srednia_ufnosc}")

#b)
#Produkty, które powinny być blisko płatków
print("---------------------------------")

platki_set = []

for i in range(0,len(rules)):
    rule = rules[i]
    left_side = list(rule.lhs)
    right_side = list(rule.rhs)
    if left_side == ['platki']:
        confidence = rule.confidence
        support = rule.support
        print(rule)
        if (confidence >= 0.3 and support >= 0.7):  #ale nie ma takich...
            if right_side not in platki_set:
                platki_set.append(right_side)

print("Produkty, które powinny być blisko płatków: ")
for produkt in platki_set:
    print(produkt)

#c)
#Produkty blisko jajek
print("---------------------------------")

jajka_set = []

for i in range(0,len(rules)):
    rule = rules[i]
    left_side = list(rule.lhs)
    right_side = list(rule.rhs)
    if right_side == ['jajka']:
        confidence = rule.confidence
        support = rule.support
        #print(rule)
        if (confidence >= 0.6 and support >= 0.3):
            if (left_side not in jajka_set):
                jajka_set.append(left_side)

print("Produkty, które wspierają sprzedaż jajek: ")
for produkt in jajka_set:
    print(produkt)
