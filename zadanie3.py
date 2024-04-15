# --- Zadanie 3 ---

#W pewnej zamkniętej społeczności liczącej 10000 osób pojawiła się osoba chora na pewną chorobę
#("pacjent 0"), co spowodowało epidemię. Wiedząc, że każda osoba chora na tę chorobę zaraża codziennie dwie
#zdrowe osoby, które od razu od tego dnia zaczynają chorować, podać przewidywany przebieg epidemii. W szczególności
#odpowiedzieć na pytanie: po ilu dniach będzie najwięcej chorych i kiedy epidemia wygaśnie z powodu braku osób
#podatnych na zachorowanie? Założyć przy tym, że choroba trwa 14 dni od dnia zarażenia i przez ten okres chorzy
#mogą zarażać inne osoby. Oprócz tego osoby, które wyzdrowiały nie mogą już zachorować.

ilosc_osob = 10000
zarazani_dzien = 2
czas_choroby = 14

chorych = 1
zdrowych = ilosc_osob - chorych
ilosc_dni = 0

while(chorych < ilosc_osob):
    if(chorych >= ilosc_osob):
        break
    else:
        #print(ilosc_dni)
        #print(chorych)
        nowi_chorzy = chorych * zarazani_dzien
        #print(f"Nowi chorzy: {nowi_chorzy}")
        ilosc_dni += 1
        chorych += nowi_chorzy
        #print(f"Chorych: {chorych}")

print(f"Po {ilosc_dni} będzie najwięcej chorych")
koniec_epidemii = ilosc_dni + czas_choroby
print(f"Epidemia wygaśnie po {koniec_epidemii} dniach")

