# --- Zadanie 6 ---

#Wykonać implementację kolejki i wykorzystać ją do wydruku 12 nazw miesięcy (najpierw nazwy miesięcy
#wstawiamy do kolejki, a poźniej pobieramy je z kolejki oraz drukujemy je na ekranie).

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

kolejka_miesiecy = Queue()

miesiace = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
for miesiac in miesiace:
    kolejka_miesiecy.enqueue(miesiac)

print("Nazwy miesięcy:")
while not kolejka_miesiecy.is_empty():
    print(kolejka_miesiecy.dequeue())
