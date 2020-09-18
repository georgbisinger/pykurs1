# Mehrere Datensätze in eine sqlite-Datenbank schreiben
import os
import sqlite3
from sqlite3 import Error

curPfad = os.path.dirname(__file__)
txtPfad = os.path.join(curPfad, "Material/MusikTitelUpdate.txt")

titelListe = []

with open(txtPfad, mode="r", encoding="Utf-8") as fh:
    for zeile in fh:
        if zeile[-1] == "\n":
            zeile = zeile[:-1]
        titelListe.append(zeile.split(","))

print(titelListe)

dbPfad = os.path.join(curPfad, r"Material\\PyMusik.db")

conDb = None

try:
    # Schritt 1: Verbindung herstellen
    conDb = sqlite3.connect(dbPfad)
    # Schritt 2: Cursor anlegen
    cursorDb = conDb.cursor()
    # Schritt 3: SQL-Kommando festlegen
    sqlCmd = "Insert Into Titel (Titel,Interpret,Jahr,Kategorie,Bewertung,Laenge) Values (?,?,?,?,?,?)"
    # Schritt 3: Ausführen des Insert-Kommandos
    cursorDb.executemany(sqlCmd, titelListe)
    # Schritt 4: Commit
    conDb.commit()
    print(f"*** {len(titelListe)} Titel wurden in die Datenbank geschrieben ***")
    # Schritt 5: Select-Abfrage ausführen
    cursorDb = conDb.execute("Select * From Titel")
    # Schritt 5: Hole alle Datensätze als Liste
    alleTitel = cursorDb.fetchall()
    for titel in alleTitel:
        print(titel)

except Error as e:
    print(f"!!! Fehler beim Herstellen der Verbindung ({e})")
finally:
    if not conDb is None:
        conDb.close()
        print("*** Die Verbindung wurde wieder geschlossen ***")
