# Ein Dictionary als Diagramm mit etwas mehr Komfort
# Ein Dictionary als Diagramm so einfach wie möglich
import matplotlib.pyplot as plt
import os

# Einen absoluten Pfad zu bilden ist nur dann erforderlich, wenn sich py- und txt-Datei nicht im selben Verzeichnis befinden
# __file__ steht immer für den Verzeichnispfad der Py-Datei
staedteDateipfad = os.path.dirname(__file__)
staedteDateipfad = os.path.join(staedteDateipfad, "Material/Staedte2.txt")

staedte = {}
# staedte = dict()

with open(staedteDateipfad, mode='r', encoding='utf-8') as fh:
    for zeile in fh:
        if zeile[-1] == "\n":
           zeile = zeile[:-1]
        # Sehr elegante Zuweisung der drei Listenelemente an drei Variablen!
        stadt, kfz, einwohner = zeile.split(",")
        # Gibt es den Namen der Stadt bereits als Schlüssel?
        if not staedte.get(stadt):
            staedte[stadt] = []
        staedte[stadt] = (stadt, kfz, einwohner)

print("%d Städte eingelesen." % len(staedte))

for stadt, kfzEinw in staedte.items():
    # Warum ist das "Type Casting" per int() erforderlich?
    print("Name: %s Kfz-Kennzeichen: %s Einwohner: %d" % (stadt, kfzEinw[1], int(kfzEinw[2])))

einwohner = [int(value[2]) for value in staedte.values()]

bars = plt.bar(staedte.keys(), einwohner)

Farben = ["blue", "orange", "lightgreen", "red", "lightblue", "green", "pink", "yellow"]

for i, bar in enumerate(bars):
    bar.set_facecolor(Farben[i])

plt.title("Städte im Landkreis Esslingen")
plt.ylabel("Einwohner")

# Dank Mr. Google findet man solche Kleinigkeiten, ohne "stundenlang" die offizielle Dokumentation
# lesen zu müssen

plt.gcf().canvas.set_window_title("Ein Dictionary als Diagramm")
plt.gcf().set_size_inches(10,8)


plt.show()

