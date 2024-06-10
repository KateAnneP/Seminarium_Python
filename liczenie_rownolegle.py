#Program, gdzie są dwa procesy liczące równoelgle
#Ekspetyment, który porówna efektywność czasową, operacje w środku wiele razy np. 1000
#Wersja bez żadnej równoległości też 1000 razy. Czy wersja z równoległością jest szybsza i ile razy szybsza.

#(2,33 + 1,71) * (5,99 - 2.71)

from multiprocessing import Process, Queue
from timeit import default_timer as timer

a = 2.33
b = 1.71
c = 5.99
d = 2.71

def fun1(queue):
    wynik =  a + b
    queue.put(wynik)

def fun2(queue):
    wynik = c - d
    queue.put(wynik)

def rownolegle():
    # Równolegle 1000 razy:
    queue = Queue()

    start = timer()

    procesy = []
    for _ in range(1000):
        p1 = Process(target=fun1, args=(queue,))
        p2 = Process(target=fun2, args=(queue,))
        procesy.append((p1, p2))
        p1.start()
        p2.start()

    wyniki = []
    for p1, p2 in procesy:
        p1.join()
        p2.join()
        wyniki.append((queue.get(), queue.get()))

    wynik_koncowy = 0
    for wynik_p1, wynik_p2 in wyniki:
        wynik_koncowy += wynik_p1 * wynik_p2

    end = timer()
    print(f"Czas wykonania równoległego: {end - start} sekund")

def nie_rownolegle():
    #1000 razy wykonanie bez równoległości
    start = timer()

    wyniki = []
    for _ in range(1000):
        wynik_p1 = a + b
        wynik_p2 = c - d
        wyniki.append((wynik_p1, wynik_p2))

    wynik_koncowy = 0
    for wynik_p1, wynik_p2 in wyniki:
        wynik_koncowy += wynik_p1 * wynik_p2

    end = timer()
    print(f"Czas wykonania sekwencyjnego: {end - start} sekund")

def main():

    queue = Queue()

    p1 = Process(target=fun1, args=(queue,))
    p2 = Process(target=fun2, args=(queue,))

    start_p1 = timer() #Start procesów
    p1.start()

    start_p2 = timer()
    p2.start()

    p1.join()   #Koniec procesów
    end_p1 = timer()

    p2.join()
    end_p2 = timer()

    wynik_p1 = queue.get()  #Pobieranie wyników z kolejki
    wynik_p2 = queue.get()
    wynik = wynik_p1 * wynik_p2

    end = timer()

    time1 = end_p1 - start_p1
    time2 = end_p2 - start_p2
    time_final = end - start_p1

    print(f"Proces p1 time: {time1}")
    print(f"Proces p2 time: {time2}")
    print(f"Final time: {time_final}")

if __name__ == '__main__':
    #main()
    #rownolegle()
    nie_rownolegle()


