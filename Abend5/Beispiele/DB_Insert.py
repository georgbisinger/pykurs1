# Insert-Kommando mit einer SQLite-Datenbank

from os import path
import sqlite3
from sqlite3 import Error

# Nur bei VSCode erforderlich bzw. wenn sich die py-Datei nicht im aktuellen Verzeichnis befindet

curPfad = path.dirname(__file__)
dbPfad = path.join(curPfad, r"Material\\PyMusik.db")

conDb = None

try:
    # Schritt 1: Verbindung herstellen
    conDb = sqlite3.connect(dbPfad)
    # Schritt 2: Zusammenstellen des SQL-Kommandos Insert Into
    sqlCmd = "Insert Into Titel Values(26, 'Westend boys','Petshop Boys',1985,'Pop',4,3.55)"
    # Schritt 3: Ausführen des Insert-Kommandos
    conDb.execute(sqlCmd)
    # Schritt 4: Select-Abfrage ausführen
    cursorDb = conDb.execute("Select * From Titel")
    # Schritt 5: Hole alle Datensätze als Liste
    alleTitel = cursorDb.fetchall()
    for titel in alleTitel:
        print(titel)

    # Schritt 6: Neuen Datensatz wieder löschen
    conDb.execute("Delete From Titel Where Id=26")

except Error as e:
    print(f"!!! Fehler beim Herstellen der Verbindung ({e})")
finally:
    if not conDb is None:
        conDb.close()
        print("*** Die Verbindung wurde wieder geschlossen ***")
