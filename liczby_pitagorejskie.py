#Liczby pitagorejskie - trójki:
#x^2 + y^2 = z^2
#x, y, z należy do {1,2,..., N}
#np. N = 50
# Napisać to pętlą i zmierzyć czas
# Potem użyć wątków, np. 3,5, obliczyć i zmierzyć czas

from multiprocessing import Process, Queue
from timeit import default_timer as timer

def liczby_pitagorejskie_petla(N):
    trojki = []
    for x in range(1, N + 1):
        for y in range(x, N + 1):  # Startujemy od x, aby uniknąć duplikatów
            for z in range(y, N + 1):  # Startujemy od y, aby uniknąć duplikatów
                if x * x + y * y == z * z:
                    trojki.append((x, y, z))
    return trojki
def liczby_pitagorejskie_watki(start, end, queue):
    trojki = []
    for x in range(start, end):
        for y in range(x, end):  # Startujemy od x, aby uniknąć duplikatów
            for z in range(y, end):  # Startujemy od y, aby uniknąć duplikatów
                if x * x + y * y == z * z:
                    trojki.append((x, y, z))
    queue.put(trojki)

def main():
    N = 50

    #pętla
    start = timer()
    trojki = liczby_pitagorejskie_petla(N)
    end = timer()
    czas = end - start
    print("Czas podczas wykonywania pętli: ", czas)
    print("Odnalezione trójki: ", trojki)

    #wątki
    queue = Queue()
    threads = []

    liczba_watkow = 5
    porcja = N//liczba_watkow

    start = timer()

    for i in range(liczba_watkow):
        start = i * porcja + 1
        end = (i + 1) * porcja + 1 if i != liczba_watkow - 1 else N + 1
        thread = Process(target=liczby_pitagorejskie_watki, args=(start, end, queue))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    trojki2 = []
    while not queue.empty():
        trojki2.extend(queue.get())

    end = timer()
    czas = end - start
    print("Czas przy podziale na wątki: ", czas)
    print("Odnalezione trójki: ", trojki2)


if __name__ == '__main__':
    main()