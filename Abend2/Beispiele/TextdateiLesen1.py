# Eine Textdatei Zeile für Zeile einlesen
import os

txtDateiPfad = os.path.dirname(__file__)
txtDateiPfad = os.path.join(txtDateiPfad, "../Material/Gewichtsdaten.txt")

fs = open(txtDateiPfad, 'r', encoding='utf-8')
# Ausgabe der Kopfzeile
zeile = fs.readline()
print(zeile)
# Durchlaufen der restlichen Zeilen
for zeile in fs:
    print(zeile)
fs.close()

# Warum wird immer eine Leerzeile zwischendrin ausgegeben
    