# Das erste Python-Programm zum Ausprobieren
# Gibt jeweils einen Fakt über Python aus
import os
import random

aktuellerPfad = os.path.abspath(os.path.dirname(__file__)) 
dateiPfad = os.path.join(aktuellerPfad, "Pythonfakten.txt") 

# Eine leere Liste für die Fakten anlegen
fakten = []

# Alle Textzeilen einlesen
with open(dateiPfad, "r") as fhandle:
    # Immer daran denken: Es kommt auf die Groß-/Kleinschreibung an
        fakten = fhandle.readlines()

# Jetzt eine Zufallszahlen zwischen 0 und Anzahl der Fakten "ziehen"

z = random.randint(0, len(fakten))

# Jetzt einen Satz ausgeben
# Wichtig: Hier kann ein Fehler auftreten - wer hat eine Idee warum?
print(fakten[z])