# --- Zadanie 4 ---

#Napisz program, który realizuje grę komputerową o nazwie: kamień, papier i nożyce.
#W tej grze użytkownik komputera gra z komputerem. Odbywa się to w ten sposób, że komputer pyta użytkownika co
#wybiera: kamień, papier czy nożyce.
#Jeśli użytkownik poda tę informację z klawiatury (np. jedną z liczb 1, 2 lub 3), to wtedy komputer losuje
#swój ruch (czyli także wybiera jedną z trzech wymienionych rzeczy), po czym informuje użytkownika o wyniku
#rozgrywki. Zasady gry są takie: kamień wygrywa z nożycam (bo nożyce nie mogą go przeciąć) ale
#przegrywa z papierem (bo za pomocą papieru potrafimy owinąć kamień), natomiast papier przegrywa z nożycami
#(bo nożyce łatwo przetną papier).
#Dwa jednakowe przedmioty dają remis. Gra ma zapewnić wielokrotną rozgrywkę w czasie jednego uruchomienia programu,
#zliczając uzyskane punkty gracza i komputera.

import random as rnd
import os

punkty_gracza = 0
punkty_komputera = 0

print("*** Kamień, papier, nożyce ***")
print("Instrukcja: Wprowadź liczbę, aby wybrać twój ruch. Ruch komputera jest losowy.")
print("1 - kamień")
print("2 - papier")
print("3 - nożyce")
print("     0 - zakończenie gry")

ruch = int(input("Wybierz twój ruch: "))

while(ruch != 0):
    print("-----------------------------------------------")
    if(ruch == 1):
        print("Wybrałeś kamień")
    elif(ruch == 2):
        print("Wybrałeś papier")
    elif(ruch == 3):
        print("Wybrałeś nożyce")

    ruch_komputera = rnd.randint(1,3)
    if (ruch_komputera == 1):
        print("Ruch komputera: kamień")
    elif (ruch_komputera == 2):
        print("Ruch komputera: papier")
    elif (ruch_komputera == 3):
        print("Ruch komputera: nożyce")

    if(ruch_komputera == ruch):
        print("Remis!!!")
        punkty_gracza = punkty_gracza + 1
        punkty_komputera = punkty_komputera + 1
    elif (ruch == 1 and ruch_komputera == 3):
        print("Wygrywasz!!!")
        punkty_gracza = punkty_gracza + 1
    elif (ruch == 3 and ruch_komputera == 1):
        print("Przegrywasz!!!")
        punkty_komputera = punkty_komputera + 1
    elif(ruch_komputera > ruch):
        print("Przegrywasz!!!")
        punkty_komputera = punkty_komputera + 1
    elif(ruch_komputera < ruch):
        print("Wygrywasz!!!")
        punkty_gracza = punkty_gracza + 1

    print(f"Punkty gracza: {punkty_gracza}")
    print(f"Punkty komputera: {punkty_komputera}")

    print("--------------------------------------------------------")
    print("1 - kamień")
    print("2 - papier")
    print("3 - nożyce")
    ruch = int(input("Czy chcesz grać dalej? Wprowadź swój ruch: "))
    if (ruch == 0 and (punkty_komputera != 0 or punkty_gracza != 0)):
        print("Wynik końcowy: ")
        print(f"Punkty gracza: {punkty_gracza}")
        print(f"Punkty komputera: {punkty_komputera}")

