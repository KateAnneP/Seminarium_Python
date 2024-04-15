# --- Zadanie 5 ---

#Dana jest następująca kolekcja zbiorów:
# {a,b,c,d}, {a,b}, {b,a,c}, {b,d}, {d,e}, {a}, {b,e}, {b,d}, {a,c,e}, {a,b,c,d,e}"
#Napisz program, który wyszukuje takie podzbiory z powyższej kolekcji, które są najmniejsze w sensie relacji inkluzji,
#tzn. dla każdego z takich podzbiorów nie istnieje w kolekcji inny podzbiór, którego ten podzbiór byłby podzbiorem
#właściwym.

kolekcja = [
    {'a', 'b', 'c', 'd'},
    {'a', 'b'},
    {'b', 'a', 'c'},
    {'b', 'd'},
    {'d', 'e'},
    {'a'},
    {'b', 'e'},
    {'b', 'd'},
    {'a', 'c', 'e'},
    {'a', 'b', 'c', 'd', 'e'}
]

najmniejsze_podzbiory = []

for zbior in kolekcja:
    jest_najmniejszy = True
    for inny_zbior in kolekcja:
        if zbior != inny_zbior and zbior.issubset(inny_zbior):
            jest_najmniejszy = False
            break
    if jest_najmniejszy:
        najmniejsze_podzbiory.append(zbior)

print("Najmniejsze podzbiory:")
for podzbior in najmniejsze_podzbiory:
    print(podzbior)
