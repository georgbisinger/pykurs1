# Import einer Py-Datei aus einem anderen Verzeichnis
# Das Unterverzeichnis VHSModul enthält die Datei MeineFunctions.py
# So nicht
# import VHSModul

# Führt zu einem Fehler
# import MeineFunctions

import sys

# Pfad muss absolut angegeben werden
sys.path.append("d:\\Pykiste\\VHSKurs\\Kursabende\\Abend4\\VHSModul")
print(sys.path)

from MeineFunctions import *

print(Kennwort(8))

print(Zufallszahl(1,100))

print(Zufallszahl())