# Eine Liste per Iterator ansprechen

staedte = ["Göppingen", "Nürtingen", "Kirchheim Teck", "Esslingen", "Plochingen", "Böblingen", "Stuttgart"]

staedteIter = iter(staedte)

# Bringt nichts, da eine Liste bereits einen Iterator darstellt
for stadt in staedteIter:
    print(stadt)

# Ab hier wird es leider etwas komplizieter - das ist eher etwas für den Fortgeschrittenen Kurs
class StaedteIterator:

    def __init__(self, Liste, Anzahl):
        self.Liste = Liste
        self.MaxAnzahl = Anzahl
        self.Zaehler = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.Zaehler < self.MaxAnzahl:
            self.Zaehler += 1
            return self.Liste[self.Zaehler]
        else:
            return None

print()

staedteIter = StaedteIterator(staedte, 3)

while True:
    stadt = next(staedteIter)
    if stadt == None:
        break
    print(stadt)
