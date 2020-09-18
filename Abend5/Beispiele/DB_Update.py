# Update-Kommando mit einer sqlite-Datenbank

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
    # Schritt 2: Zusammenstellen des SQL-Kommandos Update
    # Der Titel des Datensatzes mit Id=26 soll aktualisiert werden
    sqlCmd = "Update Titel Set Titel=? Where Id=26"
    # Schritt 3: Ausführen des Update-Kommandos
    neuerTitel = ["Eastend Girls"]
    conDb.execute(sqlCmd, neuerTitel)
    # Schritt 4: Änderung bestätigen
    conDb.commit()
    print("*** Die Aktualisierung wurde durchgeführt. ***")
    # Schritt 5: Select-Abfrage für das Abrufen aller Titel ausführen
    cursorDb = conDb.execute("Select * From Titel")
    alleTitel = cursorDb.fetchall()
    for titel in alleTitel:
        print(titel)
except Error as e:
    print(f"!!! Fehler beim Herstellen der Verbindung ({e})")
finally:
    if not conDb is None:
        conDb.close()
        print("*** Die Verbindung wurde wieder geschlossen ***")
