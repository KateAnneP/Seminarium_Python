# --- Zadanie 1 ---

#Napisz program Kalkulator, który pozwala wykonywać cztery podstawowe działania na ułamkach dziesiętnych
#(dodawanie, odejmowanie, mnożenie i dzielenie). Weź po uwagę, że dzielenie liczb wymiernych nie jest zawsze
#wykonalne.

print("*** Kalkulator ***")
print('Instrukcja: ')
print('0 - wyjście z programu')
print('1 - dodawanie')
print('2 - odejmowanie')
print('3 - mnożenie')
print('4 - dzielenie')

dzialanie = input('Podaj działanie, jakie chcesz wykonać: ')

while(dzialanie != '0'):
    a = int(input('Podaj liczbę: '))
    b = int(input('Podaj drugą liczbę: '))
    if dzialanie == '1':
        print(f"{a} + {b} = {a + b}")
    elif dzialanie == '2':
        print(f"{a} - {b} = {a - b}")
    elif dzialanie == '3':
        print(f"{a} * {b} = {a * b}")
    elif dzialanie == '4':
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Dzielenie przez 0 jest niedozwolone!")
    else:
        print("Podano nieprawidłowe działanie!")

    dzialanie = input("Czy chcesz liczyć dalej? Podaj kolejną akcję: ")
