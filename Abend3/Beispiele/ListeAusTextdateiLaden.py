# Liste aus einer Textdatei laden

import os

# Einen absoluten Pfad zu bilden ist nur dann erforderlich, wenn sich py- und txt-Datei nicht imselben Verzeichnis befinden
# __file__ steht immer für den Verzeichnispfad der Py-Datei
staedteDateipfad = os.path.dirname(__file__)
staedteDateipfad = os.path.join(staedteDateipfad, "Material/Staedte.txt")

staedte = []
# staedte = list()

with open(staedteDateipfad, mode='r', encoding='utf-8') as fh:
    for zeile in fh:
        if zeile[-1] == "\n":
           zeile = zeile[:-1]
        staedte.append(zeile)

for stadt in staedte:
    print("%s ist eine Stadt in der Region" % stadt)

