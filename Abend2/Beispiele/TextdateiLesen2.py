# Eine Textdatei Zeile für Zeile einlesen
import os

txtDateiPfad = os.path.dirname(__file__)
txtDateiPfad = os.path.join(txtDateiPfad, "../Material/Gewichtsdaten.txt")

with open(txtDateiPfad, 'r', encoding='utf-8') as fs:
    # Ausgabe der Kopfzeile
    zeile = fs.readline()
    # Abschneiden des letzten LineFeed-Zeichens (ASCII Code 10) per Slicing
    print(zeile[:-1])
    # Durchlaufen der restlichen Zeilen
    for zeile in fs:
        print(zeile[:-1])

